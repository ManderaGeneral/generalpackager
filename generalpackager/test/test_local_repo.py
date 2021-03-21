
from generalfile import Path
from generalpackager.api.local_repo import LocalRepo

import unittest


class TestLocalRepo(unittest.TestCase):
    """ Skipped tests:
    """
    def test_get_first_repo(self):
        self.assertEqual(LocalRepo("generalpackager"), LocalRepo.get_first_repo())

    def test_has_metadata(self):
        self.assertEqual(True, LocalRepo().has_metadata())
        self.assertEqual(False, LocalRepo(Path().absolute().get_parent(2, 2)).has_metadata())













































