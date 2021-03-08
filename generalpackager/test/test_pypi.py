
from generalpackager.api.pypi import PyPI
from generalfile.test.setup_workdir import setup_workdir
from generalfile import Path

import unittest


class TestPyPI(unittest.TestCase):
    """ Skipped tests:
    """
    def test_exists(self):
        self.assertEqual(True, PyPI("generalpackager").exists())
        self.assertEqual(False, PyPI("random-package_that,cant.exist").exists())

    def test_get_tarball_url(self):
        pypi = PyPI("generalpackager")
        self.assertEqual(True, pypi.name in pypi.get_tarball_url())
        self.assertEqual(True, pypi.name in pypi.get_tarball_url(version="1.0.0"))

    def test_download_and_unpack_tarball(self):
        setup_workdir(use_working_dir=True)

        path = PyPI("generalpackager").download_and_unpack_tarball(target_folder="repo")
        self.assertEqual(True, "generalpackager" in next(path.get_paths_in_folder()))

        with self.assertRaises(AttributeError):
            PyPI("generalpackager").download_and_unpack_tarball(target_folder="repo", version="0.0.111")

        path = PyPI("generalpackager").download_and_unpack_tarball(target_folder="repo", version="0.0.11", overwrite=True)
        self.assertEqual(2, len(list(path.get_paths_in_folder())))

