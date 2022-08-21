
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
    def _resolve_path_localmodule(cls, name):
        """ :param generalpackager.Packager cls:
            :rtype: Path or None """
        localmodule = cls.LocalModule(name=name)
        if localmodule.exists():
            path = localmodule.path.get_parent_repo()
            Log().debug(f"Found path {path} for {name}. Modules path is {localmodule.path}.")
            return path

    @classmethod
    def _resolve_path_workingdir_traverse_parents(cls, name):
        """ :param generalpackager.Packager cls:
            :rtype: Path or None """
        repo_parent_path: Path = Path().absolute().get_parent(depth=-1, include_self=True, traverse_excluded=True, filt=lambda path, name_=name: (path / name_).is_repo())
        if repo_parent_path is not None:
            return repo_parent_path / name

    @classmethod
    def _resolve_path(cls, name):
        """ :param generalpackager.Packager cls:
            :rtype: Path or None """
        # for method in (cls._resolve_path_workingdir_traverse_parents, ):
        for method in (cls._resolve_path_localmodule, cls._resolve_path_workingdir_traverse_parents):
            path = method(name=name)
            if path:
                Log().debug(f"Resolved path with '{method.__name__}' for '{name}', got '{path}'.")
                return path

    @classmethod
    def _scrub_path(cls, name, path):
        """ :param generalpackager.Packager cls:
            :rtype: Path or None """
        name = cls._scrub_name(name=name)

        if path is None:
            path = cls._resolve_path(name=name)

        if path is not None:
            path = Path(path).absolute()

            if not path.endswith(name):
                raise AttributeError(f"Path '{path}' seems to be wrong for '{name}'. Workdir is '{Path().absolute()}'.")

        return path


