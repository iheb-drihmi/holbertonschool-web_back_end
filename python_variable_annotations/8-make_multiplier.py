#!/usr/bin/env python3
"""
A function that takes a float
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that
    """

    return lambda x: x * multiplier
