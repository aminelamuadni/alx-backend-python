#!/usr/bin/env python3
"""Module for safely retrieving a value from a dictionary with a default."""


from typing import TypeVar, Mapping, Any, Union, Optional

T = TypeVar('T')  # Declare TypeVar for return and default types


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Optional[T] = None) -> Union[T, None]:
    """Retrieve value from a dictionary based on given key or return default.

    Args:
        dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
        key (Any): The key to look for in the dictionary.
        default (Optional[T]): The default value to return if the key is not
        found.

    Returns:
        Union[T, None]: The value associated with the key, or the default.
    """
    return dct.get(key, default)
