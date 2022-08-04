

from generalpackager import Packager
from generalfile.test.setup_workdir import setup_workdir

import unittest


class TestPackager(unittest.TestCase):
    # Packager.spawn_children  # Skipped test
    # Packager.spawn_parents  # Skipped test

    def test_name(self):
        self.assertEqual("generalpackager", Packager().name)




