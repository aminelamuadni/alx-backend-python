#!/usr/bin/env python3
"""Module for summing a list of floats."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum all floats in a list and return the sum.

    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The sum of the list elements.
    """
    return sum(input_list)
