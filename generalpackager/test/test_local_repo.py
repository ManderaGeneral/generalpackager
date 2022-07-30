
from generallibrary import Ver
from generalpackager.api.localrepo.base.localrepo import LocalRepo
from generalfile import Path
import generalpackager

import unittest

import importlib

class TestLocalRepo(unittest.TestCase):
    # LocalRepo.pip_install  # Skipped test
    # LocalRepo.pip_uninstall  # Skipped test
    # LocalRepo.unittest  # Skipped test
    # LocalRepo.create_sdist  # Skipped test
    # LocalRepo.upload  # Skipped test
    # LocalRepo.get_path_from_name  # Skipped test
    # LocalRepo.get_repo_path_parent  # Skipped test
    # LocalRepo.write_metadata  # Skipped test

    @classmethod
    def setUpClass(cls):
        path = Path(generalpackager.__file__).get_parent(1, 1)  # type: Path
        path.set_working_dir()

    def test_metadata_exists(self):
        self.assertEqual(True, LocalRepo().metadata_exists())  # HERE **
        self.assertEqual(False, LocalRepo("doesntexist").metadata_exists())

    def test_load_metadata(self):
        self.assertEqual(True, LocalRepo().metadata.enabled)
        self.assertEqual("generalpackager", LocalRepo().name)
        self.assertIsInstance(LocalRepo().metadata.version, Ver)
        self.assertIsInstance(LocalRepo().metadata.description, str)
        self.assertIsInstance(LocalRepo().metadata.install_requires, list)
        self.assertIsInstance(LocalRepo().metadata.extras_require, dict)
        self.assertIsInstance(LocalRepo().metadata.topics, list)
        self.assertIsInstance(LocalRepo().metadata.manifest, list)

    def test_get_metadata_dict(self):
        self.assertEqual(True, LocalRepo().get_metadata_dict()["enabled"])

    def test_exists(self):
        self.assertEqual(True, LocalRepo().exists())
        self.assertEqual(True, LocalRepo.repo_exists(LocalRepo().path))

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
            "get_test_path",
            "get_init_path",
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
        version = local_repo.metadata.version
        local_repo.bump_version()
        self.assertNotEqual(local_repo.metadata.version, version)
        self.assertIn("metadata.json", local_repo.git_changed_files())
        local_repo.metadata.version = version
        self.assertEqual(local_repo.metadata.version, version)

    def test_get_repo_path_child(self):
        self.assertNotEqual(None, LocalRepo.get_repo_path_child(LocalRepo().path.get_parent()))
        self.assertEqual(None, LocalRepo.get_repo_path_child(LocalRepo().path))































