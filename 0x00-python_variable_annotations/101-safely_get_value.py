#!/usr/bin/env python3
"""Module for safely retrieving a value from a dictionary with a default."""


from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')  # Generic type variable for flexible typing


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Retrieve value from a dictionary based on a given key or return default.

    Args:
        dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None]): The default value to return if the key is not
        found.

    Returns:
        Union[Any, T]: The value associated with the key, or the default. This
        allows for returning any type.
    """
    if key in dct:
        return dct[key]
    else:
        return default
