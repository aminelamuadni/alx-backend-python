#!/usr/bin/env python3
"""Module for creating a multiplier function."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a given float by a specified multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the
        multiplier.
    """
    return lambda x: x * multiplier
