
import unittest
import random

from generalpackager import GitHub


# Running tests locally:            Set env var 'packager_github_api' to GitHub token, run unittests with PyCharm as usual
# Running tests in GitHub Actions:  Run test.main and supply env vars as launch options.

class TestGitHub(unittest.TestCase):
    def test_topics(self):
        github = GitHub("generalpackager")

        original_values = github.get_topics()

        value = str(random.randint(0, 99999))
        github.set_topics(value)
        self.assertEqual([value], github.get_topics())

        github.set_topics(*original_values)
        self.assertEqual(original_values, github.get_topics())

        # github.assert_url_up()
