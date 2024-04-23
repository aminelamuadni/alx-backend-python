#!/usr/bin/env python3
"""
This module provides a function to measure the average execution time
of an asynchronous function that spawns multiple asynchronous tasks.
"""


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the execution time of wait_n divided by the number of executions.

    Args:
        n (int): The number of times to spawn wait_n.
        max_delay (int): The maximum delay that can be passed to wait_n.

    Returns:
        float: The average time per execution.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
