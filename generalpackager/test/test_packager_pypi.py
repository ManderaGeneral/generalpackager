

from generalpackager import Packager
from generalfile.test.setup_workdir import setup_workdir

import unittest


class TestPackager(unittest.TestCase):
    def test_compare_local_to_pypi(self):
        setup_workdir(use_working_dir=True)
        packager = Packager()
        self.assertGreater(len(packager.compare_local_to_pypi()), 0)

    def test_get_latest_release(self):
        self.assertIn("CE", str(Packager().get_latest_release()))


