#!/usr/bin/env python3
"""tests the client module"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient, get_json


class TestGithubOrgClient(unittest.TestCase):
    """tests the githuborgclient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.GithubOrgClient.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test the org method of GithubOrgClient"""

        # Set up the mock get_json method to return a specific value
        mock_get_json.return_value = {"login": org_name}

        # Create an instance of GithubOrgClient with the org_name
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org()

        # Check that get_json was called exactly once with the correct argument
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/"
                                              f"{org_name}")

        # Check that the result is as expected
        self.assertEqual(result, {"login": org_name})
