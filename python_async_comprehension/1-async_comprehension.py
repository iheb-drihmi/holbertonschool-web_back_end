#!/usr/bin/env python3
"""
The coroutine will collect 10 random
"""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    The coroutine will collect 10 random
    '''
    return [value async for value in async_generator()]
