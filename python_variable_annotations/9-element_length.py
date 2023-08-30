#!/usr/bin/env python3
"""
A function that returns values
"""

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns value with
    """
    return [(i, len(i)) for i in lst]
