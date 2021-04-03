

from generalpackager import Packager
from generalfile.test.setup_workdir import setup_workdir

import unittest


class TestPackager(unittest.TestCase):
    """ Skip:
        GenerateFile
        generate """
    def test_relative_path_is_aesthetic(self):
        packager = Packager()
        self.assertEqual(False, packager.relative_path_is_aesthetic("setup.py"))
        self.assertEqual(True, packager.relative_path_is_aesthetic("README.md"))
        self.assertEqual(True, packager.relative_path_is_aesthetic(packager.localrepo.get_readme_path()))

    def test_filter_relative_filenames(self):
        packager = Packager()
        self.assertEqual(["setup.py"], packager.filter_relative_filenames("setup.py", aesthetic=None))
        self.assertEqual(["setup.py"], packager.filter_relative_filenames("setup.py", aesthetic=False))
        self.assertEqual([], packager.filter_relative_filenames("setup.py", aesthetic=True))

    def test_compare_local_to_remote(self):
        setup_workdir(use_working_dir=True)  # HERE ** Not right in github actions
        packager = Packager()
        print(packager.compare_local_to_remote())
        self.assertGreater(len(packager.compare_local_to_remote()), 0)

    def test_generate_setup(self):
        packager = Packager()
        text = packager.generate_setup()
        self.assertIn(str(packager.localrepo.version), text)
        self.assertIn(str(packager.localrepo.name), text)

    def test_generate_manifest(self):
        packager = Packager()
        text = packager.generate_manifest()
        self.assertIn("include metadata.json", text)

    def test_generate_git_exclude(self):
        packager = Packager()
        text = packager.generate_git_exclude()
        self.assertIn(".idea", text)

    def test_generate_license(self):
        packager = Packager()
        text = packager.generate_license()
        self.assertIn("Mandera", text)

    def test_generate_workflow(self):
        packager = Packager()
        text = packager.generate_workflow()
        self.assertIn("runs-on", text)

    def test_generate_readme(self):
        packager = Packager()
        text = str(packager.generate_readme())
        self.assertIn("pip install", text)

    def test_generate_personal_readme(self):
        packager = Packager()
        text = str(packager.generate_personal_readme())
        self.assertIn("generallibrary", text)



