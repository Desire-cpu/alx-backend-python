#!/usr/bin/env python3
'''
Task 3's module.
'''
import asyncio

# Importing the wait_random function from the '0-basic_async_syntax' module
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Creates an asynchronous task for wait_random.

    Args:
        max_delay: The maximum delay for the wait_random function.

    Returns:
        An asyncio.Task representing the asynchronous task.
    '''
    # Create an asynchronous task for the wait_random function
    return asyncio.create_task(wait_random(max_delay))
