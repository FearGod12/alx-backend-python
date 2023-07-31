#!/usr/bin/env python3
"""tests the client module"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient, get_json


class TestGithubOrgClient(unittest.TestCase):
    """tests the githuborgclient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test the org method of GithubOrgClient"""

        # Set up the mock get_json method to return a specific value
        mock_get_json.return_value = {"login": org_name}

        # Create an instance of GithubOrgClient with the org_name
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Check that get_json was called exactly once with the correct argument
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/"
                                              f"{org_name}")

        # Check that the result is as expected
        self.assertEqual(result, {"login": org_name})

    def test_public_repos_url(self):
        """tests _public_repos_url"""
        TEST_PAYLOAD = {
            "repos_url": "https://api.github.com/orgs/example-org/repos"
        }
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_repo:
            mock_repo.return_value = TEST_PAYLOAD
            test_instance = GithubOrgClient("google")
            result = test_instance._public_repos_url
            self.assertEqual(result,
                             "https://api.github.com/orgs/example-org/repos")
