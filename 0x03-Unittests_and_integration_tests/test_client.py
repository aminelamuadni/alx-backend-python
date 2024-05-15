#!/usr/bin/env python3
"""
This module tests the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that the GithubOrgClient.org method correctly uses get_json to
        retrieve org information.

        Args:
            org_name (str): The name of the GitHub organization to retrieve.
            mock_get_json (MagicMock): A mock of the get_json function.
        """
        url = f"https://api.github.com/orgs/{org_name}"
        test_data = {'login': org_name, 'id': 12345}
        mock_get_json.return_value = test_data

        github_org_client = GithubOrgClient(org_name)
        response = github_org_client.org

        # Assert get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(url)

        # Assert the response from .org is as expected
        self.assertEqual(response, test_data)


if __name__ == '__main__':
    unittest.main()
