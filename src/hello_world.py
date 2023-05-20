import sys
from datetime import datetime

import anyio
import dagger
import pytz


async def create_container():
    # Initialize dagger client.
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        # Set pipeline action.
        python = (
            # Generate docker container.
            client.container()
            # Pull docker image.
            .from_("python:3.11-slim-buster")
            # Execute command on docker container.
            .with_exec(["python", "-V"])
        )

        # execute.
        version = await python.stdout()

    sysdate = pytz.timezone('Asia/Tokyo').localize(datetime.now())
    print(f"Hello ! Dagger SDK Python: {version} {sysdate.strftime('%Y/%m/%d %H:%M:%S')}")


if __name__ == "__main__":
    anyio.run(create_container)
