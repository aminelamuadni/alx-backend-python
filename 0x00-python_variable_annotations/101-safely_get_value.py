#!/usr/bin/env python3
"""
This module provides a utility function for safely retrieving values from a
dictionary.
It uses type annotations for flexible type handling.
"""


from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Retrieve a value from a dictionary using a key with a fallback to a default
    value.

    Args:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional): The value to return if the key is
        not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key or the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
