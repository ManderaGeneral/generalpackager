
from generallibrary import Recycle, AutoInitBases, Log
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
    DEFAULT_OWNER = ...

    # _recycle_keys = {"owner": lambda owner: _SharedOwner._scrub_owner(owner=owner)}
    _recycle_keys = {"owner": lambda cls, owner: cls._scrub_owner(owner=owner)}

    def __init__(self, owner=None):
        self.owner = self._scrub_owner(owner=owner)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        assert cls.DEFAULT_OWNER is not Ellipsis

    @classmethod
    def _scrub_owner(cls, owner):
        return owner or cls.DEFAULT_OWNER


class _LocalRepo_Path:
    _recycle_keys = {"path": lambda path: str(_LocalRepo_Path._scrub_path(path=path))}

    def __init__(self, path=None):
        self.path = self._scrub_path(path=path)

    @classmethod
    def _scrub_path(cls, path):
        return Path(path).absolute()


class _Packager_Path:
    _recycle_keys = {"path": lambda cls, name, path: str(cls._scrub_path(name=name, path=path))}

    def __init__(self, name=None, path=None):
        self.path = self._scrub_path(name=name, path=path)

    @classmethod
    def _localmodule_resolve_path(cls, name):
        """ :param generalpackager.Packager cls:
            :rtype: Path or None """
        localmodule = cls.LocalModule(name=name)
        if localmodule.exists():
            path = localmodule.path.get_parent_repo()
            return path

    @classmethod
    def _workingdir_resolve_path(cls, name):
        """ :param generalpackager.Packager cls:
            :rtype: Path or None """
        path = Path(name)
        if path.is_repo():
            return path

    @classmethod
    def _resolve_path(cls, name):
        """ :param generalpackager.Packager cls:
            :rtype: Path or None """
        methods = (
            cls._localmodule_resolve_path,
            cls._workingdir_resolve_path,
        )

        for method in methods:
            path = method(name=name)
            if path:
                Log().debug(f"Resolved path with '{method.__name__}' for '{name}', got '{path}'.")
                return path

    @classmethod
    def _scrub_path(cls, name, path):
        """ :param generalpackager.Packager cls:
            :rtype: Path or None """
        if path is None:
            path = cls._resolve_path(name=name)

        if path is not None:
            path = Path(path).absolute()

            if not path.endswith(name):
                raise AttributeError(f"Path '{path}' seems to be wrong for '{name}'.")

        return path


