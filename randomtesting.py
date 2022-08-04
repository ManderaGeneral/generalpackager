from generalpackager import *

from generalfile import Path


# print(Packager().get_ordered_packagers())

# for packager in Packager().get_all():  # type: Packager
#     print(packager, packager.get_parents())


module = LocalModule("generallibrary")
print(module.get_dependencies())

packager = Packager("generallibrary")
# print(packager.localmodule.get_dependencies())
print(packager.get_dependencies())  # HERE ** Not right
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


