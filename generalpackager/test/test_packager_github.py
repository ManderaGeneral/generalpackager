

from generalpackager import Packager
from generalfile.test.setup_workdir import setup_workdir

import unittest


class TestPackager(unittest.TestCase):
    Packager.sync_github_metadata  # Skipped test
    Packager.commit_and_push  # Skipped test

    # def test_clone_repo(self):
    #     setup_workdir(use_working_dir=True)
    #     self.assertEqual(True, Packager().clone_repo("").exists())

