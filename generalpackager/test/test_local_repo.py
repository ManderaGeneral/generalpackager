
from generalfile import Path
from generalpackager.api.local_repo import LocalRepo

import unittest


class TestLocalRepo(unittest.TestCase):
    """ Skipped tests:
        commit_and_push
        pip_install
        unittest
        create_sdist
        upload
    """
    def test_get_first_repo(self):
        self.assertEqual(LocalRepo("generalpackager"), LocalRepo.get_first_repo())
        self.assertEqual(LocalRepo.get_first_repo_path(), LocalRepo.get_first_repo_path("foo/bar"))
        path = Path().absolute().get_parent(2, 2)
        self.assertEqual(None, LocalRepo.get_first_repo_path(path))
        self.assertEqual(path, LocalRepo.scrub_path(path))

    def test_has_metadata(self):
        self.assertEqual(True, LocalRepo().has_metadata())
        self.assertEqual(False, LocalRepo(Path().absolute().get_parent(2, 2)).has_metadata())

    def test_load_metadata(self):
        self.assertEqual("generalpackager", LocalRepo().name)

    def test_exists(self):
        self.assertEqual(True, LocalRepo().exists())
        self.assertEqual(True, LocalRepo.path_exists(LocalRepo().path))

    def test_get_local_repos(self):
        self.assertEqual(LocalRepo().path.get_parent(), LocalRepo.get_repos_path())

    def test_paths(self):
        method_names = (
            "get_readme_path",
            "get_metadata_path",
            "get_git_exclude_path",
            "get_setup_path",
            "get_manifest_path",
            "get_license_path",
            "get_workflow_path",
            "get_test_path"
        )
        local_repo = LocalRepo()
        for name in method_names:
            self.assertEqual(True, getattr(local_repo, name)().exists())

    def test_get_test_paths(self):
        self.assertLess(2, len(list(LocalRepo().get_test_paths())))

    def test_text_in_tests(self):
        self.assertEqual(True, LocalRepo().text_in_tests("stringthatexists"))
        self.assertEqual(False, LocalRepo().text_in_tests("stringthat" + "doesntexist"))

    def test_get_package_paths(self):
        package_paths = list(LocalRepo().get_package_paths_gen())
        self.assertIn(LocalRepo().get_test_path(), package_paths)
        self.assertIn(LocalRepo().path / LocalRepo().name, package_paths)
        self.assertNotIn(LocalRepo().path, package_paths)

    def test_get_changed_files(self):
        local_repo = LocalRepo()
        version = local_repo.version
        local_repo.bump_version()
        self.assertNotEqual(local_repo.version, version)
        self.assertIn("metadata.json", local_repo.get_changed_files())
        local_repo.version = version
        self.assertEqual(local_repo.version, version)

































