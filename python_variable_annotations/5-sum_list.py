#!/usr/bin/env python3
"""
a type-annotated function
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum
    """

    return sum(input_list)
