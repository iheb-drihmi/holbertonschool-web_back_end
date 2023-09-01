#!/usr/bin/env python3
"""
the total runtime is roughly 10 seconds, 
"""


from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    the total runtime is roughly 10 seconds, 
    '''

    first_time = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    next_time = time()

    return next_time - first_time
