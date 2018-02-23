import time
import asyncio


def now(): return time.time()


async def do_some_work(x):
    print("Waiting:", x)


def callback(feature):
    print("Callback:", feature.result())


start = now()

coroutine = do_some_work(2)

loop = asyncio.get_event_loop()

# task = asyncio.ensure_future(coroutine)

# task.add_done_callback(callback)

# loop.run_until_complete(task)
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)



print("TIME:", now() - start)
