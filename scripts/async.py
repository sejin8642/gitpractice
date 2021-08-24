# Scripts to test the understanding of asyncio module
import asyncio

counter = 0

async def a():
    global counter

    for _ in range(100):
        counter += 2
        print(counter)
        await asyncio.sleep(0)

async def b():
    global counter

    for _ in range(100):
        counter -= 1
        print(counter)
        await asyncio.sleep(0)

future = asyncio.gather(a(), b())
asyncio.get_event_loop().run_until_complete(future)

