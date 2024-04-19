#!/usr/bin/env python3
"""Module for summing a mixed list of integers and floats."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum all numbers in a mixed list (integers and floats) and return the sum
    as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The list containing integers and
        floats to sum.

    Returns:
        float: The sum of the list elements.
    """
    return float(sum(mxd_lst))
