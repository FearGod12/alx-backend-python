#!/usr/bin/env python3
"""test module for the utils
and all its methods"""

from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized
from unittest.mock import patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    """tests for utils class
    and its methods"""

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, result):
        """test the access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """tests the access_nested map method
        and its return value"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """tests the get_json method
    and its return value"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """tests get_+json
        and its return value"""
        response = mock_get.return_value
        response.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once()
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """tests memoization
    for testing purpose"""

    def test_memoize(self):
        """Test memoization of a_property method
        to test if it caches"""

        # Define the TestClass with a_method and a_property
        class TestClass:
            """class to be used for testing
            purpose only"""
            def a_method(self):
                """memoized method
                to be cached"""
                return 42

            @memoize
            def a_property(self):
                """calls a_method
                and see if it caches"""
                return self.a_method()

        # Patch the a_method
        with patch.object(TestClass, "a_method") as mock_a_method:
            # Create an instance of TestClass
            test_class_instance = TestClass()

            # Call a_property twice
            result1 = test_class_instance.a_property()
            result2 = test_class_instance.a_property()

            # Check that a_method was called only once
            mock_a_method.assert_called_once()

            # Check that the results are equal
            self.assertEqual(result1, result2)
