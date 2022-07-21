
from generalpackager import Packager, LocalRepo



localrepo = LocalRepo("").extended()
print(LocalRepo.cls_target_classes)
print(type(localrepo).__name__)

# class A:
#     def __init_subclass__(cls):
#         print(cls)
#
# class C:
#     pass
#
# class B(C, A):
#     pass
#



