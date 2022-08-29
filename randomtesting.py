from generalpackager import *

# print(Packager("generallibrary").localrepo.unittest())

# print(LocalRepo())


# Log().configure_stream()

print(Packager("pandas").localrepo.is_general())


from typing import TypeVar

_BarCls = TypeVar("_BarCls", bound="Bar")


class Foo:
    @classmethod
    def method(cls: _BarCls):
        cls.hi()

class Bar(Foo):
    def hi(self):
        pass

