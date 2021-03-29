

from generalpackager import Packager
from generalfile.test.setup_workdir import setup_workdir

import unittest


class TestPackager(unittest.TestCase):
    """ Skipped:
        sync_github_metadata"""
    def test_sync_github_metadata(self):
        setup_workdir(use_working_dir=True)
        print(Packager().clone_repo(path="x"))

