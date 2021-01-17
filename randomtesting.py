
from generallibrary import TreeDiagram, ObjInfo
from generalpackager import Packager, LocalModule, PyPI, GitHub

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




# def dynamic_property(cls, key, getter, setter):
#     setattr(cls, key, property(getter, setter))
#
#
# class A:
#     pass
#
# key = "foo"
# dynamic_property(A, key, lambda self, key=key: getattr(self, f"_{key}", ...), lambda self, value, key=key: setattr(self, f"_{key}", value))
#
# a = A()
# a.foo = 2
#
# b = A()
# b.foo = 3
#
# print(a.foo)
# print(b.foo)


class PackageGrp:
    """ Handles a collection of packages. """
    def __init__(self):
        self.packages = [Packager(name) for name in Packager.get_users_packages()]


print(PackageGrp().packages)

# print(PyPI.get_users_packages("Mandera").intersection(GitHub.get_users_packages("ManderaGeneral")))
# print(PyPI.get_users_packages("Mandera"))
# print(GitHub.get_users_packages("ManderaGeneral"))


# Todo: Write [CI MAJOR] in commit message to bump major for example.
# Todo: Push empty commits to dependents after publish in workflow.
# Todo: Generate GitHub profile readme.
# Todo: Compare local_repo version with pypi version before publishing.

# Old workflow failed as we got duplicates in dependents for some reason, but I'm thinking we'll ignore that as we're moving to replace it.
