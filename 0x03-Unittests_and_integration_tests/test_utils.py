#!/usr/bin/env python3
"""test module for the utils"""

from utils import access_nested_map, get_json
import unittest
from parameterized import parameterized
from unittest.mock import patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    """tests for utils class"""

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
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """tests the get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """tests get_+json"""
        response = mock_get.return_value
        response.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once()
        self.assertEqual(result, test_payload)
