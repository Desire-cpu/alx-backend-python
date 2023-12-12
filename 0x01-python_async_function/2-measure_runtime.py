#!/usr/bin/env python3
"""
This script demonstrates the measurement of time for concurrent coroutines.

This module contains a function, measure_time, which calculates the average time to generate a list of random values using concurrent coroutines.
"""

import time
from asyncio import run

# Importing the wait_n function from the '1-concurrent_coroutines' module
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the time taken to generate a list of random values using concurrent coroutines.

    Args:
        n: The number of times to generate a random value.
        max_delay: The maximum random time generated.

    Returns:
        The average time to generate a list of random values.
    """

    # Record the start time
    start: float = time.time()

    # Run the wait_n function to generate random values concurrently
    run(wait_n(n, max_delay))

    # Record the end time
    end: float = time.time()

    # Calculate and return the average time per generated value
    return (end - start) / n
