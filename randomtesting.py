
from generallibrary import TreeDiagram, ObjInfo
import generallibrary
from generalpackager import *
from generalfile import Path


packager = Packager("generalpackager")
packager.setup_all("Added automatic version bumping.")



# class A:
#     """ Tools to help Path interface a Local Python Repository. """
#
#     name = ...
#     version = ...
#     description = ...
#     install_requires = ...
#     extras_require = ...
#     topics = ...
#
#     metadata_keys = [key for key, value in locals().items() if value is Ellipsis]
#
#     def __init__(self):
#         for key in self.metadata_keys:
#             setattr(A, key, property(
#                 lambda self, key=key: getattr(self, f"_{key}", ...),
#                 lambda self, value, key=key: self.metadata_setter(self, value, f"_{key}"),
#             ))
#
#     @staticmethod
#     def metadata_setter(self, value, key):
#         print("yo")
#         setattr(self, key, value)
#
#
#
# a = A()
# a.name = "foo"
# print(a.name)
# print(a._name)
