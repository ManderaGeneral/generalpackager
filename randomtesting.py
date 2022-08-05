from generalpackager import *

from generalfile import Path

from generallibrary import Recycle


# print(Packager().get_ordered_packagers())

# for packager in Packager().get_all():  # type: Packager
#     print(packager, packager.get_parents())


def names(x):
    print(sorted([y.name for y in x]))


packager = Packager()
# packager = Packager("generallibrary")

print(LocalModule("generallibrary").path)


# names(packager.get_dependencies())
#
# module = LocalModule("generallibrary")
# names(module.get_dependencies())
#
#
#
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


