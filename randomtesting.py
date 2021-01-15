
from generallibrary import TreeDiagram, ObjInfo
from generalpackager import Packager, LocalModule, PyPI

import generallibrary
import generalpackager
from generalfile import Path


# packager = Packager("generalpackager")

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



class PackageGrp:
    """ Handles a collection of packages. """
    def __init__(self):
        self.packages = [Packager(name) for name in PyPI.get_users_packages("Mandera")]


print(PackageGrp().packages)


# Todo: Write [CI MAJOR] in commit message to bump major for example.
# Todo: Push empty commits to dependents after publish in workflow.
# Todo: Generate GitHub profile readme.
# Todo: Compare local_repo version with pypi version before publishing.

# Old workflow failed as we got duplicates in dependents for some reason, but I'm thinking we'll ignore that as we're moving to replace it.
