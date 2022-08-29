

import unittest

from generalpackager import Packager


class TestPackager(unittest.TestCase):
    def test_name(self):
        self.assertEqual("generalpackager", Packager().name)

    def test_all_packages(self):
        all_packages = Packager.Packages.all_packages()



