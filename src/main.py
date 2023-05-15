import asyncio
import datetime

import novelcraft.sdk as sdk
import random

async def main():
    await sdk.initialize()
    # sdk.get_logger().info('Hello, world!')

    start_time = datetime.datetime.now()

    while True:
        if (datetime.datetime.now() - start_time).total_seconds() > 60:
            break

        # Required to keep the SDK alive
        await asyncio.sleep(0.1)

        agent = sdk.get_agent()

        if agent is None:
            continue
        # basic agent, rand movement
        n = random.randint(0, 4)
        if n == 0:
            agent.set_movement(sdk.MovementKind.STOPPED)
        elif n == 1:
            agent.set_movement(sdk.MovementKind.FORWARD)
        elif n == 2:
            agent.set_movement(sdk.MovementKind.BACKWARD)
        elif n == 3:
            agent.set_movement(sdk.MovementKind.LEFT)
        elif n == 4:
            agent.set_movement(sdk.MovementKind.RIGHT)

    await sdk.finalize()
    # sdk.get_logger().info('Goodbye, world!')

if __name__ == '__main__':
    asyncio.run(main())
