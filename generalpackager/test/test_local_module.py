
from generalpackager.api.local_module import LocalModule

import unittest


class TestLocalModule(unittest.TestCase):
    """ Skipped tests:
    """
    def test_exists(self):
        self.assertEqual(True, LocalModule("generalpackager").exists())
