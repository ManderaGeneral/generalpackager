

from generalpackager.api.pypi import PyPI
from generalfile.test.setup_workdir import setup_workdir
from generallibrary import Date

import unittest


class TestPyPI(unittest.TestCase):
    def test_compare_local_to_pypi(self):
        setup_workdir(use_working_dir=True)

        path = PyPI("generalpackager").download_and_unpack_tarball(target_folder="repo")