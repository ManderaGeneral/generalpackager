
from generallibrary import TreeDiagram, ObjInfo
from generalpackager import Packager, LocalModule, PyPI, GitHub, LocalRepo
import generallibrary
import generalpackager
from generalfile import Path

import subprocess
import sys
import re







packager = Packager("generalpackager")
packager.file_workflow.generate()

# print(packager.localrepo.version)
# packager.localrepo.bump_version()
# print(packager.localrepo.version)

# print(packager.get_changed_files(aesthetic=False))
# print(packager.get_changed_files(aesthetic=True))
# print(packager.pypi.get_version())


# packager.localmodule.get_dependants("generallibrary")
# packager.generate_readme()
# packager.generate_localfiles()
# packager.sync_package("Cleaned up secrets, testing auto")
# packager.localrepo.get_todos()
# packager.sync_github_metadata()
# packager.generate_git_exclude()
# packager.generate_setup()

# packager.localrepo.get_git_exclude_path().open_folder()

# print(GitHub.is_creatable("generalpackager", "ManderaGeneral"))
# print(LocalModule.is_creatable("generalpackager"))
# print(LocalRepo.is_creatable(packager.path))
# print(PyPI.is_creatable("generalpackager"))



class PackageGrp:
    """ Handles a collection of packages. """
    def __init__(self, repos_path=None):
        self.repos_path = LocalRepo.get_repos_path(path=repos_path)

        self.packagers = []
        self.load_general_packages()

    def load_general_packages(self):
        """ Load my general packages. """
        self.add_packages(*Packager.get_users_packages())

    def add_packages(self, *names):
        """ Add a Package. """
        self.packagers.extend([Packager(name=name, repos_path=self.repos_path) for name in names])

    def clone(self):
        """ Clone all packages to repos_path. """
        for packager in self.packagers:
            packager.clone_repo()

    def install(self):
        """ Install all packages. """
        for packager in self.packagers:
            packager.localrepo.pip_install()

    def get_bumped(self):
        """ Get a list of bumped packagers, meaning PyPI version and LocalRepo version mismatch. """
        # return [(packager.localrepo.version, packager.pypi.get_version()) for packager in self.packagers if packager.is_bumped()]
        return [packager for packager in self.packagers if packager.is_bumped()]

    # def test(self):



# path = Path().absolute().get_parent(1) / "testrepos"
# path.open_folder()

# packageGrp = PackageGrp()
# print(packageGrp.packagers)
# print(packageGrp.get_bumped())




# Todo: Write [CI MAJOR] in commit message to bump major for example.
# Todo: Push empty commits to dependents after publish in workflow.
# Todo: Generate GitHub profile readme.
# Todo: Compare local_repo version with pypi version before publishing.

# Old workflow failed as we got duplicates in dependents for some reason, but I'm thinking we'll ignore that as we're moving to replace it.
