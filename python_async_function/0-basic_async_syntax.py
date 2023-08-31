#!/usr/bin/env python3
"""
an asynchronous coroutine that take
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay
    between 0 and max_delay.
    """

    Delay = max_delay * random.random()
    await asyncio.sleep(Delay)
    return Delay
