
from generallibrary import Recycle, AutoInitBases

from generalpackager.other.packages import Packages


class _SharedAPI(Recycle, metaclass=AutoInitBases):
    """ Shared by Packager and all APIs. """
    @staticmethod
    def name_is_general(name):
        return name in Packages.all_packages()

    def is_general(self):
        return self.name_is_general(name=self.name)

    @property
    def simple_name(self):
        return self.name.replace("general", "")  # Make this work for NPM's "gen" too


class _SharedName:
    """ Shared by Packager, LocalModule, GitHub and PyPI. """  # HERE ** Maybe this should be in LocalRepo too after all, that way is_general can work
    DEFAULT_NAME = "generalpackager"

    _recycle_keys = {"name": lambda name: _SharedName._scrub_name(name=name)}

    def __init__(self, name=None):
        self.name = self._scrub_name(name=name)

    @classmethod
    def _scrub_name(cls, name):
        return name or cls.DEFAULT_NAME


class _SharedOwner:
    """ Shared by GitHub, PyPI and NPM. """
    DEFAULT_OWNER = "Mandera"

    _recycle_keys = {"owner": lambda owner: _SharedOwner._scrub_owner(owner=owner)}

    def __init__(self, owner=None):
        self.owner = self._scrub_owner(owner=owner)

    @classmethod
    def _scrub_owner(cls, owner):
        return owner or cls.DEFAULT_OWNER



