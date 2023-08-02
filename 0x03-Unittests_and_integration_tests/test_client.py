#!/usr/bin/env python3
"""tests the client module
for learning integration tests"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient, get_json


class TestGithubOrgClient(unittest.TestCase):
    """tests the githuborgclient class
    with all the methods and attruibutes"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test the org method of GithubOrgClient
        and test the org method"""

        # Set up the mock get_json method to return a specific value
        mock_get_json.return_value = {"login": org_name}

        # Create an instance of GithubOrgClient with the org_name
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Check that get_json was called exactly once with the correct argument
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/{}".
                                              format(org_name))

        # Check that the result is as expected
        self.assertEqual(result, {"login": org_name})

    def test_public_repos_url(self):
        """tests _public_repos_url
        and its return value"""
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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """test the public repos method
        and the return value"""
        TEST_PAYLOAD = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = TEST_PAYLOAD
        public_repos_url_payload =\
            "https://api.github.com/orgs/example-org/repos"
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = public_repos_url_payload

            client = GithubOrgClient("example-org")
            result = client.public_repos()
            mock_get_json.assert_called_once()
            mock_repos.assert_called_once()

            self.assertEqual(result, ['repo1', 'repo2'])
