#!/usr/bin/env python3
"""
This module contains unittests for testing the functionality of the
access_nested_map function found in the utils module. The tests are
designed to ensure that the function behaves as expected under various
scenarios using the parameterized test approach.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Dict, Mapping, Sequence, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class houses the unittests for the access_nested_map
    function. It utilizes a parameterized test method to check multiple
    scenarios to ensure the function extracts values correctly according to a
    provided path within a nested dictionary.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict[Any, Any],
                               path: Tuple[Any, ...], expected: Any) -> None:
        """
        Test the functionality of the access_nested_map function with a given
        nested map and path. This test asserts that the function returns the
        correct output for specified input paths.

        Args:
            nested_map (Dict[Any, Any]): The nested dictionary to be accessed.
            path (Tuple[Any, ...]): A tuple containing the sequence of keys to
                                    follow in the nested dictionary.
            expected (Any): The expected result after following the path in the
                            nested dictionary.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        Test that a KeyError is raised for invalid paths in the nested map.

        Args:
            nested_map (Mapping): The nested dictionary to be accessed.
            path (Sequence): The path to be tested, which should raise a
                             KeyError.
            message (str): The expected exception message.

        Asserts:
            A KeyError is raised with the specific message.
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()