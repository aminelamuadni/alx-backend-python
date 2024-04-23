#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that waits for a random delay.
"""


import asyncio
import random
from typing import Coroutine


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay seconds and
    returns it.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay time that was waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
