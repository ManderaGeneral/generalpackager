

from generalpackager import Packager

import unittest


class TestPackager(unittest.TestCase):
    def test_name(self):
        self.assertEqual("generalpackager", Packager().name)




