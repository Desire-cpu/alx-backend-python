#!/usr/bin/env python3
'''
Task last module.
'''

import asyncio
from typing import List

# Importing the task_wait_random function from the '3-tasks' module
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Executes task_wait_random n times.

    Args:
        n: The number of times to execute the task_wait_random function.
        max_delay: The maximum delay for the task_wait_random function.

    Returns:
        A sorted list of float values representing the execution times.
    '''
    # Use asyncio.gather to execute task_wait_random asynchronously n times
    wait_t = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )

    # Return a sorted list of execution times
    return sorted(wait_t)
