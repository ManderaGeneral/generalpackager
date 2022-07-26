""" Methods specific for my general packages.
    Isolatable methods are put inside APIs.

    Todo: Prevent workflow using pypi to install a general package. """

from generallibrary import NetworkDiagram, deco_cache
from generalpackager.api.shared import _SharedAPI, _SharedName
from generalpackager.api.localrepo.base.localrepo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.github import GitHub
from generalpackager.api.pypi import PyPI

from generalpackager.packager_files import _PackagerFiles
from generalpackager.packager_github import _PackagerGitHub
from generalpackager.packager_markdown import _PackagerMarkdown
from generalpackager.packager_metadata import _PackagerMetadata
from generalpackager.packager_pypi import _PackagerPypi
from generalpackager.packager_workflow import _PackagerWorkflow
from generalpackager.packager_relations import _PackagerRelations

from generalpackager.other.packages import Packages


class Packager(_SharedAPI, _SharedName, NetworkDiagram, _PackagerMarkdown, _PackagerGitHub, _PackagerFiles, _PackagerMetadata, _PackagerPypi, _PackagerWorkflow, _PackagerRelations):
    """ Uses APIs to manage 'general' package.
        Contains methods that require more than one API as well as methods specific for ManderaGeneral. """

    author = 'Rickard "Mandera" Abraham'
    email = "rickard.abraham@gmail.com"
    license = "mit"
    python = "3.8", "3.9"  # Only supports basic definition with tuple of major.minor
    os = "windows", "ubuntu"  # , "macos"

    git_exclude_lines = npm_ignore_lines = ".idea", "dist", ".git", "test/tests"
    git_exclude_lines += "build", "*.egg-info", "__pycache__", "PKG-INFO", "setup.cfg"
    npm_ignore_lines += "node_modules", ".parcel-cache"

    Packages = Packages

    _recycle_keys = _SharedAPI._recycle_keys.copy()
    _recycle_keys["path"] = str

    _SENTINEL = object()

    def __init__(self, name=None, path=None, target=_SENTINEL, github_owner=None, pypi_owner=None):
        self._name = name
        self._path = path
        self._target = target
        self._github_owner = github_owner
        self._pypi_owner = pypi_owner

    @property
    @deco_cache()
    def localrepo(self):
        return LocalRepo(path=self._path).targetted(target=self._target)

    @property
    @deco_cache()
    def github(self):
        return GitHub(name=self._name, owner=self._github_owner)

    @property
    @deco_cache()
    def localmodule(self):
        if self.target == self.localrepo.Targets.python:
            return LocalModule(name=name)

    @property
    @deco_cache()
    def pypi(self):
        return PyPI(name=name, owner=pypi_owner)

    @property
    def target(self):
        if self._target is self._SENTINEL:
            return self.localrepo.metadata.target
        else:
            return self._target

    @staticmethod
    def summary_packagers():
        return [
            Packager(name="Mandera", github_owner="Mandera"),
            Packager(name=".github", github_owner="ManderaGeneral"),
        ]

    @property
    def path(self):
        if not self.localrepo.exists() and self.localmodule.exists():
            return self.localrepo.get_repo_path_parent(self.localmodule.path)
        return self.localrepo.path

    @property
    def simple_name(self):
        return self.name.replace("general", "")

    def spawn_children(self):
        """ :param generalpackager.Packager self: """
        for packager in self.get_dependants(only_general=True):
            if packager.localrepo.enabled:
                packager.set_parent(parent=self)

    def spawn_parents(self):
        """ :param generalpackager.Packager self: """
        for packager in self.get_dependencies(only_general=True):
            if packager.localrepo.enabled:
                self.set_parent(parent=packager)

    # def exists(self):  # Not sure why we should have this seems ambigous
    #     """ Just check GitHub for now. """
    #     return self.github.exists()

    def __repr__(self):
        return f"<Packager [{self.package_type}]: {self.name}>"

















































