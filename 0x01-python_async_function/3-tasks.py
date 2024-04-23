#!/usr/bin/env python3
"""
This module provides a function that creates an asyncio.Task from a coroutine.
"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that runs a coroutine which waits for a random
    delay.

    Args:
        max_delay (int): The maximum delay in seconds before the task
        completes.

    Returns:
        asyncio.Task: The task object that runs the coroutine.
    """

    return asyncio.create_task(wait_random(max_delay))
