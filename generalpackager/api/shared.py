
from generallibrary import Recycle, AutoInitBases



class _SharedAPI(Recycle, metaclass=AutoInitBases):
    """ Shared by Packager, LocalModule, GitHub and PyPI. """
    DEFAULT_NAME = "generalpackager"

    _recycle_keys = {"name": lambda name: _SharedAPI._scrub_name(name=name)}

    def __init__(self, name=None):
        self.name = self._scrub_name(name=name)

    @classmethod
    def _scrub_name(cls, name):
        return name or cls.DEFAULT_NAME

    @staticmethod
    def name_is_general(name):
        return name.startswith("general") or name in ("manderageneral", )

    def is_general(self):
        """ Just use name for now, can generalize in the future.

            :param generalpackager.api.pypi.PyPI or generalpackager.api.local_module.LocalModule or generalpackager.api.local_repo.LocalRepo or generalpackager.api.github.GitHub self: """
        return self.name_is_general(name=self.name)



class _SharedGitAndRepo(_SharedAPI):
    DEFAULT_OWNER = ...

    _recycle_keys = _SharedAPI._recycle_keys.copy()
    _recycle_keys["owner"] = lambda owner: _SharedGitAndRepo._scrub_owner(owner=owner)

    def __init__(self, name=None, owner=None):
        self.owner = self._scrub_owner(owner=owner)

    @classmethod
    def _scrub_owner(cls, owner):
        return owner or cls.DEFAULT_OWNER



