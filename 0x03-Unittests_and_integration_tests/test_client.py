#!/usr/bin/env python3
"""
This module tests the GithubOrgClient class.
"""

import unittest
from unittest.mock import PropertyMock, patch
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

    def test_public_repos_url(self):
        """
        Test that the _public_repos_url property returns the correct URL
        based on the mocked org payload.
        """
        json_payload = {
            'repos_url': 'https://api.github.com/orgs/google/repos'
            }
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = json_payload
            github_org_client = GithubOrgClient('google')
            repos_url = github_org_client._public_repos_url

            self.assertEqual(repos_url, json_payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Tests that public_repos method returns a correctly parsed list of
        repositories from a mocked JSON response and verifies that necessary
        methods and properties are called.
        """
        mock_repo_url = 'https://api.github.com/orgs/google/repos'
        json_payload = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_get_json.return_value = json_payload

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = mock_repo_url
            github_org_client = GithubOrgClient('google')
            repos = github_org_client.public_repos()

            # Check that the returned list of repos is correct
            self.assertEqual(repos, ['repo1', 'repo2'])

            # Ensure that get_json was called once with the correct URL
            mock_get_json.assert_called_once_with(mock_repo_url)

            # Verify that the _public_repos_url property was accessed once
            mock_repos_url.assert_called_once()


if __name__ == '__main__':
    unittest.main()
