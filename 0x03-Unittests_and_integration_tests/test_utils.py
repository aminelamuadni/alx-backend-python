#!/usr/bin/env python3
"""
This module contains unittests for testing the functionality of the
access_nested_map function found in the utils module. The tests are
designed to ensure that the function behaves as expected under various
scenarios using the parameterized test approach.
"""

import unittest

from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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


class TestGetJson(unittest.TestCase):
    """
    Test case class for testing the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the get_json function to ensure it returns the correct payload
        for different URLs without making actual HTTP calls.

        Args:
            test_url (str): The URL to be tested.
            test_payload (dict): The expected JSON payload returned from the
                                 URL.
            mock_get: The mock object for the requests.get call.
        """
        # Configure the mock to return a response object with a .json() method
        mock_get.return_value.json.return_value = test_payload

        # Call the function with the test URL
        result = get_json(test_url)

        # Ensure get_json returns the correct payload
        self.assertEqual(result, test_payload)

        # Check that requests.get was called exactly once with the test URL
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class contains unit tests for the `memoize` decorator.
    It verifies that memoization properly caches the method output to
    prevent redundant calculations.
    """

    def test_memoize(self):
        """
        Tests the memoize decorator by ensuring a method is only executed once
        when its memoized property is accessed multiple times.
        """

        class TestClass:
            """
            Test class with a method and a memoized property.
            """

            def a_method(self):
                """
                Simulates a method that would ideally perform a calculation.
                """
                return 42

            @memoize
            def a_property(self):
                """
                Memoized property designed to cache the result of a_method.
                """
                return self.a_method()

        # Create an instance of TestClass
        test_obj = TestClass()
        with patch.object(test_obj, 'a_method',
                          return_value=42) as mocked_method:
            # Access the memoized property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            # Ensure the results are consistent
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Verify a_method was called exactly once
            mocked_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
