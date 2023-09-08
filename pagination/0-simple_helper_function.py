#!/usr/bin/env python3
"""function named index_range that takes two integer arguments"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """return"""
    i: int = page_size * page - page_size
    return (i, page_size * page)
