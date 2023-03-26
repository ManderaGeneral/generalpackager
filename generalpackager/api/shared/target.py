from typing import Literal

from generallibrary import deco_cache, flatten
from generallibrary.objinfo.objinfo import DataClass

_TARGETS_LITERAL = Literal["python", "node", "django", "exe", "summary"]

class Targets(DataClass):
    python = "python"
    node = "node"
    django = "django"
    exe = "exe"
    summary = "summary"

_DEFAULT_TARGET = Targets.python

class _SharedTarget:
    """ Used by LocalRepo and Packager """
    Targets = Targets

    @classmethod
    def target_names(cls):
        """ :param generalpackager.Packager or generalpackager.LocalRepo cls: """
        return cls.Targets.field_values_defaults()

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

    def is_summary(self):
        """ :param generalpackager.Packager or generalpackager.LocalRepo self: """
        return self.target == Targets.summary


class Packages(Targets):
    """ Purpose is to easily see if name is general and what target it has. """
    python = [
        "generaltool",
        "generalimport",
        "generallibrary",
        "generalfile",
        "generalvector",
        "generalgui",
        "generalbrowser",
        "generalpackager",
    ]
    node = [
        "genlibrary",
        "genvector",
    ]
    django = [

    ]
    exe = [
        "generalmainframe",
    ]
    summary = [
        "Mandera",
        ".github",
    ]

    @classmethod
    @deco_cache()
    def all_packages(cls):
        return flatten(cls.field_values_defaults())
