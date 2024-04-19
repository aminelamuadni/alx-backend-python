#!/usr/bin/env python3
"""Module for safely retrieving the first element of a sequence."""


from typing import Any, Sequence, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a sequence or None if the sequence is empty.

    Args:
        lst (Sequence[Any]): A sequence of any type.

    Returns:
        Optional[Any]: The first element of the sequence, or None if it is
        empty.
    """
    if lst:
        return lst[0]
    else:
        return None
