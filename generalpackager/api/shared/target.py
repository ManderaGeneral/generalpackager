from typing import Literal

from generallibrary.objinfo.objinfo import DataClass

_TARGETS_LITERAL = Literal["python", "node", "django", "exe"]

class Targets(DataClass):
    python = "python"
    node = "node"
    django = "django"
    exe = "exe"

_DEFAULT_TARGET = Targets.python

class _SharedTarget:
    Targets = Targets

    """ Used by LocalRepo and Packager """
    def is_python(self):
        """ :param generalpackager.Packager or generalpackager.LocalRepo self: """
        return self.target == Targets.python

    def is_node(self):
        """ :param generalpackager.Packager or generalpackager.LocalRepo self: """
        return self.target == Targets.node

    def is_django(self):
        """ :param generalpackager.Packager or generalpackager.LocalRepo self: """
        return self.target == Targets.django

    def is_exe(self):
        """ :param generalpackager.Packager or generalpackager.LocalRepo self: """
        return self.target == Targets.exe
