#!/usr/bin/env python3
"""tests the client module"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient, get_json


class TestGithubOrgClient(unittest.TestCase):
    """tests the githuborgclient class"""

    @parameterized(["google",
                    "abc"
                    ])
    @patch("get_json")
    def test_org(self, org, mock_get_json):
        """tests if githubOrgClient.org returns the correct value"""
        mock_get_json.return_value = "https://api.github.com/orgs/{}".\
            format(org)
        gitorg = GithubOrgClient()
        result = gitorg.org()
        mock_get_json.assert_called_once()
        self.assertEqual(result, "https://api.github.com/orgs/{}".format(org))
