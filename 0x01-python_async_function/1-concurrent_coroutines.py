#!/usr/bin/env python3
"""
This module defines a coroutine that executes another coroutine multiple
times concurrently.
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay that can be passed to wait_random.

    Returns:
        List[float]: A list of delays experienced by wait_random tasks, in the
        order that they completed.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed_delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        completed_delays.append(delay)
    return completed_delays
