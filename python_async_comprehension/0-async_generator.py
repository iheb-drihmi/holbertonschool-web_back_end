#!/usr/bin/env python3
"""
a coroutine called
"""

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
   a coroutine called
    '''
    for i in range(10):
        await sleep(1)
        yield 10 * random()
