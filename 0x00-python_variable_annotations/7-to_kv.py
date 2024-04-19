#!/usr/bin/env python3
"""
Module for converting a string and a number into a tuple with the number
squared.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple containing a string and the square of a number as a float.

    Args:
        k (str): The string to include in the tuple.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the string and the squared number
        as a float.
    """
    return (k, float(v**2))
