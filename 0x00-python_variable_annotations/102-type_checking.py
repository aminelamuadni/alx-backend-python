#!/usr/bin/env python3
"""
Module to perform element replication in lists based on a multiplication factor.
"""


from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Replicates each element in the list 'lst' a 'factor' number of times.

    Args:
        lst (List[int]): List to be zoomed.
        factor (int): Replication factor, defaults to 2.

    Returns:
        List[int]: List with replicated elements.
    """
    return [item for item in lst for _ in range(factor)]


# Example usage
array = [12, 72, 91]
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)