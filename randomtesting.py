
from generallibrary import TreeDiagram, ObjInfo
from generalpackager import Packager, LocalModule, PyPI, GitHub, LocalRepo

import generallibrary
import generalpackager
from generalfile import Path



packager = Packager("generalpackager")

print(GitHub.is_creatable("generalpackager", "ManderaGeneral"))
print(LocalModule.is_creatable("generalpackager"))
print(LocalRepo.is_creatable(packager.path))
print(PyPI.is_creatable("generalpackager"))


# HERE ** finish is_creatable, then we should really create generalcrawler (temporarily in generalpackager I guess)

# path = Path().absolute().get_parent() / "clonetest"
# packager.clone_repo(path=path)

# path.open_folder()



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




# class PackageGrp:
#     """ Handles a collection of packages. """
#     def __init__(self):
#         self.packages = []
#
#     def load_general_packages(self):
#         """ Load my general packages. """
#         self.packages.clear()
#         self.packages.extend([Packager(name) for name in Packager.get_users_packages()])
#
# print(PackageGrp().packages)

# print(PyPI.get_users_packages("Mandera").intersection(GitHub.get_users_packages("ManderaGeneral")))
# print(PyPI.get_users_packages("Mandera"))
# print(GitHub.get_users_packages("ManderaGeneral"))


# Todo: Write [CI MAJOR] in commit message to bump major for example.
# Todo: Push empty commits to dependents after publish in workflow.
# Todo: Generate GitHub profile readme.
# Todo: Compare local_repo version with pypi version before publishing.

# Old workflow failed as we got duplicates in dependents for some reason, but I'm thinking we'll ignore that as we're moving to replace it.
