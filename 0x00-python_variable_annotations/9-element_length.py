#!/usr/bin/env python3
"""Module for measuring elements' lengths within an iterable object."""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with the element and its length from an iterable of
    sequences.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a
        sequence and its length.
    """
    return [(i, len(i)) for i in lst]
