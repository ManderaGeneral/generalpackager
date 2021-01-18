
from generallibrary import TreeDiagram, ObjInfo
from generalpackager import Packager, LocalModule, PyPI, GitHub, LocalRepo

import generallibrary
import generalpackager
from generalfile import Path



packager = Packager("generalpackager")

# packager.localmodule.get_dependants("generallibrary")
# packager.upload()
# packager.generate_readme()
# packager.generate_workflow()
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
    def __init__(self, repos_path):
        self.repos_path = repos_path

        self.packagers = []

    def add_packages(self, *names):
        """ Add a Package. """
        self.packagers.extend([Packager(name=name, repos_path=self.repos_path) for name in names])

    def load_general_packages(self):
        """ Load my general packages. """
        self.add_packages(*Packager.get_users_packages())

    def clone(self):
        for packager in self.packagers:
            print(packager.path)
            # packager.clone_repo()



# path = Path().absolute().get_parent(1) / "testrepos"
#
# packageGrp = PackageGrp(repos_path=path)
# packageGrp.load_general_packages()
#
# packageGrp.clone()

from pathlib import Path

print(list(Path("C:").iterdir()))  # HERE ** https://stackoverflow.com/questions/7258993/pythons-os-listdir-behaviour-on-windows
# print(Path("C:build"))

# print(PyPI.get_users_packages("Mandera").intersection(GitHub.get_users_packages("ManderaGeneral")))
# print(PyPI.get_users_packages("Mandera"))
# print(GitHub.get_users_packages("ManderaGeneral"))


# Todo: Write [CI MAJOR] in commit message to bump major for example.
# Todo: Push empty commits to dependents after publish in workflow.
# Todo: Generate GitHub profile readme.
# Todo: Compare local_repo version with pypi version before publishing.

# Old workflow failed as we got duplicates in dependents for some reason, but I'm thinking we'll ignore that as we're moving to replace it.
