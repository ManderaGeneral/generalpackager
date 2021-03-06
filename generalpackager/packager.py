""" Methods specific for my general packages.
    Isolatable methods are put inside APIs.

    Todo: Prevent workflow using pypi to install a general package. """

from generallibrary import initBases, NetworkDiagram, Recycle
from generalpackager.api.shared import _SharedAPI
from generalpackager.api.local_repo import LocalRepo
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


@initBases
class Packager(Recycle, _SharedAPI, NetworkDiagram, _PackagerMarkdown, _PackagerGitHub, _PackagerFiles, _PackagerMetadata, _PackagerPypi, _PackagerWorkflow, _PackagerRelations):
    """ Uses APIs to manage 'general' package.
        Contains methods that require more than one API as well as methods specific for ManderaGeneral. """

    author = 'Rickard "Mandera" Abraham'
    email = "rickard.abraham@gmail.com"
    license = "mit"
    python = "3.8", "3.9"  # Only supports basic definition with tuple of major.minor
    os = "windows", "ubuntu"  # , "macos"

    git_exclude_lines = ".idea", "build", "dist", "*.egg-info", "__pycache__", ".git", "test/tests", "PKG-INFO", "setup.cfg"
    _recycle_keys = LocalModule._recycle_keys

    def __init__(self, name=None, github_owner=None, pypi_owner=None):
        self.localmodule = LocalModule(name=name)
        self.name = self.localmodule.name

        self.localrepo = LocalRepo(name=self.name)
        self.path = self.localrepo.path

        self.github = GitHub(name=self.name, owner=github_owner)
        self.pypi = PyPI(name=self.name, owner=pypi_owner)

        # Quick fix, should probably put download in a workflow step instead
        if (self.localmodule.is_general() or self.name == "Mandera") and not self.localrepo.exists():
            self.github.download(path=self.path.get_parent())

    def exists(self):
        """ Just check GitHub for now. """
        return self.github.exists()

    def spawn_children(self):
        self._spawn(self.localmodule.get_dependants(), parent=self)

    def spawn_parents(self):
        self._spawn(self.localmodule.get_dependencies(), child=self)

    def _spawn(self, modules, child=None, parent=None):
        for local_module in modules:
            if local_module.is_general():
                packager = Packager(name=local_module.name)

                if packager.localrepo.enabled:
                    (child or packager).set_parent(parent=parent or packager)

    def __repr__(self):
        return f"<Packager: {self.name}>"


















































