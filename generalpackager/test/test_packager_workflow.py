

from generalpackager import Packager
from generalfile.test.setup_workdir import setup_workdir

import unittest


class TestPackager(unittest.TestCase):
    def test_get_triggers(self):
        self.assertIn("branches", Packager().get_triggers())

    def test_step_setup_python(self):
        self.assertIn("3.8", Packager().step_setup_python("3.8"))

    def test_step_install_necessities(self):
        self.assertIn("pip install", Packager().step_install_necessities())

    def test_step_install_package_pip(self):
        self.assertIn("pip install", Packager().step_install_package_pip(*Packager().get_ordered_packagers()))

    def test_step_install_package_git(self):
        self.assertIn("pip install git", Packager().step_install_package_git(*Packager().get_ordered_packagers()))

    def test_get_env(self):
        self.assertIn("TWINE", Packager().get_env())

    def test_steps_setup(self):
        print(Packager().steps_setup())

    def test_get_unittest_job(self):
        print(Packager().get_unittest_job())

    def test_get_sync_job(self):
        print(Packager().get_sync_job())

    def test_step_run_packager_method(self):
        print(Packager().step_run_packager_method())

    def test_run_ordered_methods(self):
        print(Packager().run_ordered_methods())

    def test_workflow_unittest(self):
        print(Packager().workflow_unittest())

    def test_workflow_sync(self):
        print(Packager().workflow_sync())

    def test_if_publish_bump(self):
        print(Packager().if_publish_bump())

    def test_if_publish_publish(self):
        print(Packager().if_publish_publish())

