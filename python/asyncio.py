# -*- coding: utf8 -*-

import asyncio


async def hello():
    print("Hello world")
    await asyncio.sleep(1)
    print("Hello again")


if __name__ == '__main__':
    asyncio.run(hello())  # python 3.8

    # loop = asyncio.get_event_loop()
    # try:
    #     print("start")
    #     coroutine = hello()
    #     print("event loop")
    #     loop.run_until_complete(coroutine)
    # except:
    #     print("close")
    #     loop.close()
