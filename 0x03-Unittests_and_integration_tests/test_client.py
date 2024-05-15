#!/usr/bin/env python3
"""
This module tests the GithubOrgClient class.
"""

import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that GithubOrgClient.has_license accurately checks if the
        repository's license matches the provided license key.

        Args:
            repo (dict): The repository data containing a license key.
            license_key (str): The license key to check against the
                               repository's license.
            expected (bool): The expected result of the check.

        Tests:
            Verify that the function returns True when the license keys match,
            and False otherwise.
        """
        github_org_client = GithubOrgClient("google")
        result = github_org_client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up the mock for requests.get."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload,
            cls.repos_payload,
            cls.org_payload,
            cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop the patcher after the tests are complete."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Test the GithubOrgClient.public_repos method."""
        github_org_client = GithubOrgClient(self.org_payload["repos_url"])
        repos = github_org_client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Test the GithubOrgClient.public_repos method with a license key."""
        github_org_client = GithubOrgClient(self.org_payload["repos_url"])
        repos = github_org_client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
