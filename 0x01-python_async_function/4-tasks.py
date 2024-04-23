#!/usr/bin/env python3
"""
This module provides an asynchronous function that spawns multiple tasks,
each waiting for a random delay, and then gathers their results.
"""

import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Spawns n tasks that each wait for a random delay and then gathers their
    results.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay, in seconds, for each task.

    Returns:
        list: A list of float values representing the completion times of each
        task, ordered by their completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
