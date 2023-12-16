#!/usr/bin/env python3
'''Task 2's module.
This module measures the runtime of the async_comprehension coroutine.
'''
import asyncio
import time
from importlib import import_module as using

# Import the async_comprehension coroutine from module '1-async_comprehension'.
async_comprehension = using('1-async_comprehension').async_comprehension

# Define an asynchronous function to measure the total execution time of async_comprehension.
async def measure_runtime() -> float:
    '''Executes async_comprehension 4 times and measures the
    total execution time.
    '''
    # Record the start time.
    start_t = time.time()
    
    # Use asyncio.gather to run async_comprehension 4 times concurrently.
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    
    # Calculate the total runtime by subtracting the start time from the current time.
    return time.time() - start_t
