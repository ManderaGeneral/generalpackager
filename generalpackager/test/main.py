
import sys
import os
import unittest

from generalpackager.test.test_github import TestGitHub


import sys

from generallibrary import getFreeIndex


def get_argv_dict():
    """ Return a dict of given args from launch options.
        Uses sys.argv, attempts to split on '=', if missing then index is used as key. """
    args = {}
    for arg in sys.argv[1:]:
        if "=" in arg:
            split = arg.split("=")
            args[split[0]] = split[1]
        else:
            args[getFreeIndex(args)] = arg

    return args


print(get_argv_dict())



# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         os.environ["packager_github_api"] = sys.argv[1]
#         del sys.argv[1]
#
#     unittest.main()
