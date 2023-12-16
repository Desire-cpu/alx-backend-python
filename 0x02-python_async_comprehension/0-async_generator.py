#!/usr/bin/env python3
'''Task 0's module.
This module defines an asynchronous generator that yields a sequence of 10 random numbers.
'''
import asyncio
import random
from typing import Generator

# Define an asynchronous generator function.
async def async_generator() -> Generator[float, None, None]:
    '''Generates a sequence of 10 numbers.
    This function uses the `asyncio` module to introduce asynchronous behavior.
    It yields 10 random numbers multiplied by 10 after each second of sleep.
    '''
    for _ in range(10):
        # Asynchronously sleep for 1 second.
        await asyncio.sleep(1)
        # Yield a random number between 0 and 10.
        yield random.random() * 10
