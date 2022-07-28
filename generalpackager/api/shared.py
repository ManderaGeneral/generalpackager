
from generallibrary import Recycle, AutoInitBases
from generalfile import Path

from generalpackager.other.packages import Packages


class _SharedAPI(Recycle, metaclass=AutoInitBases):
    """ Shared by all (Packager and APIs). """
    @staticmethod
    def name_is_general(name):
        return name in Packages.all_packages()

    def is_general(self):
        """ :param generalpackager.Packager self: """
        return self.name_is_general(name=self.name)

    @property
    def simple_name(self):
        """ :param generalpackager.Packager self: """
        if self.name.startswith("general"):
            return self.name.replace("general", "")
        elif self.name.startswith("gen"):
            return self.name.replace("gen", "")
        else:
            return self.name


class _SharedName:
    """ Shared by Packager, LocalModule, GitHub and PyPI. """
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


class _SharedPath:
    """ Shared by Packager and LocalRepo. """
    _recycle_keys = {"path": lambda path: _SharedPath._scrub_path(path=path)}

    def __init__(self, path=None):
        self.path = self._scrub_path(path=path)

    @classmethod
    def _scrub_path(cls, path):
        return Path(path).absolute()


