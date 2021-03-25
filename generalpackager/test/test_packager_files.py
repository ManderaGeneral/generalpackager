

from generalpackager import Packager
from generalfile.test.setup_workdir import setup_workdir

import unittest


class TestPackager(unittest.TestCase):
    """ Skip:
        GenerateFile
        generate """
    def test_relative_path_is_aesthetic(self):
        packager = Packager()
        self.assertEqual(False, packager.relative_path_is_aesthetic("setup.py"))
        self.assertEqual(True, packager.relative_path_is_aesthetic("README.md"))
        self.assertEqual(True, packager.relative_path_is_aesthetic(packager.localrepo.get_readme_path()))

    def test_filter_relative_filenames(self):
        packager = Packager()
        self.assertEqual(["setup.py"], packager.filter_relative_filenames("setup.py", aesthetic=None))
        self.assertEqual(["setup.py"], packager.filter_relative_filenames("setup.py", aesthetic=False))
        self.assertEqual([], packager.filter_relative_filenames("setup.py", aesthetic=True))

    def test_compare_local_to_remote(self):
        pass
