from generallibrary import deco_cache

from generalpackager.api.localrepo.base.localrepo import LocalRepo
from generalpackager.api.localmodule import LocalModule
from generalpackager.api.github import GitHub
from generalpackager.api.pypi import PyPI


class _PackagerAPIs:
    LocalRepo = LocalRepo
    LocalModule = LocalModule
    GitHub = GitHub
    PyPI = PyPI

    API_NOT_AVAILABLE_ERROR = AttributeError

    def _assert_target_is_python(self):
        """ :param generalpackager.Packager self: """
        if self.target != self.localrepo.Targets.python:
            raise self.API_NOT_AVAILABLE_ERROR(f"Packager {self}'s target '{self.target}' is not '{self.localrepo.Targets.python}'")

    def _assert_not_private(self):
        """ :param generalpackager.Packager self: """
        if self.localrepo.metadata.private:
            raise self.API_NOT_AVAILABLE_ERROR(f"Packager {self} is private.")

    def _available(self, *asserts, api_name, error):
        """ :param generalpackager.Packager self: """
        try:
            for func in asserts:
                func()
        except self.API_NOT_AVAILABLE_ERROR as e:
            if error:
                raise self.API_NOT_AVAILABLE_ERROR(f"API '{api_name}' not available.")
            else:
                return False
        else:
            return True

    def localrepo_available(self, error=False):
        """ :param generalpackager.Packager self: """
        return self._available(
            api_name="LocalRepo", error=error)

    def github_available(self, error=False):
        """ :param generalpackager.Packager self: """
        return self._available(
            api_name="GitHub", error=error)

    def localmodule_available(self, error=False):
        """ :param generalpackager.Packager self: """
        return self._available(

            self._assert_target_is_python,

            api_name="LocalModule", error=error)

    def pypi_available(self, error=False):
        """ :param generalpackager.Packager self: """
        return self._available(

            self._assert_target_is_python,
            self._assert_not_private,

            api_name="PyPI", error=error)

    @property
    @deco_cache()
    def localrepo(self):
        """ :param generalpackager.Packager self: """
        """ :rtype: generalpackager.LocalRepo_Python or generalpackager.LocalRepo_Node """
        self.localrepo_available(error=True)
        return LocalRepo(path=self.path).targetted(target=self._target)

    @property
    @deco_cache()
    def github(self):
        """ :param generalpackager.Packager self: """
        self.github_available(error=True)
        return GitHub(name=self.name, owner=self._github_owner)

    @property
    @deco_cache()
    def localmodule(self):
        """ :param generalpackager.Packager self: """
        self.localmodule_available(error=True)
        return LocalModule(name=self.name)

    @property
    @deco_cache()
    def pypi(self):
        """ :param generalpackager.Packager self: """
        self.pypi_available(error=True)
        return PyPI(name=self.name, owner=self._pypi_owner)