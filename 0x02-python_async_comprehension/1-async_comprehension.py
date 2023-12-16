#!/usr/bin/env python3
"""

This module contains an asynchronous coroutine.

"""
from typing import List

# Import the asynchronous generator from module '0-async_generator'.
async_generator = __import__('0-async_generator').async_generator

# Define an asynchronous coroutine function.
async def async_comprehension() -> List[float]:
    """

    Return a list of 10 randomly generated numbers using an asynchronous comprehension.

    """
    # Use an asynchronous comprehension to generate a list of 10 numbers.
    return [i async for i in async_generator()]
