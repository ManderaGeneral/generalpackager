
import sys
import os
import unittest

from generalpackager.test.test_github import TestGitHub


if __name__ == "__main__":
    if len(sys.argv) > 1:
        os.environ["packager_github_api"] = sys.argv[1]
        del sys.argv[1]

    unittest.main()
