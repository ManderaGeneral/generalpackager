from generalpackager import *

from generalfile import Path

from generallibrary import Recycle, SigInfo



# print(Packager().get_ordered_packagers())

# for packager in Packager().get_all():  # type: Packager
#     print(packager, packager.get_parents())



"""
First issue:
    
    Packager and LocalModule get_dependencies() is returning different results
"""
# def names(x):
#     print(sorted([y.name for y in x]))
# packager = Packager()
# names(packager.get_dependencies())
# module = LocalModule()
# names(module.get_dependencies())


"""
Second issue:
    Packager's path has to be supplied even when they are very easy to retrieve
    
    Recycle keys will be an issue if we can resolve path
    
    Packager("generallibrary") and Packager("generallibrary", "./generallibrary")
"""

# Packager("generallibrary")



# print(Packager().localmodule.path.get_parent_repo())

# print(Packager("matplotlib").localrepo)

# print(LocalModule("matplotlib").path)


# print(packager.localrepo)
# print(packager.localrepo.metadata)
# print(packager.localrepo.metadata.install_requires)


# print(packager.get_parents())


# github = GitHub()
# print(github.owner)
# print(github.get_owners_packages())



# class Foo:
#     @classmethod
#     def x(cls):
#         print(cls)
#
#
# class Bar:
#     pass
#
# meth = Foo.x
# meth.__self__ = Bar
# meth()
# print(dir(Foo.x))


