#!/usr/bin/env python3
"""
This module provides a function to zoom into an array (tuple) by replicating
each element a specified number of times.
"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Expands elements of a tuple into a list by repeating each element multiple
    times.

    Args:
        lst (Tuple): Tuple of elements to be expanded.
        factor (int): The number of times each element is repeated in the
        output list. Defaults to 2.

    Returns:
        List: A list containing the repeated elements.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
