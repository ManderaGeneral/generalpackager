""" Methods specific for my general packages.
    Isolatable methods are put inside APIs.

    Todo: Add a check in workflow to make sure it doesn't use a pypi version in case of wrong order. """

from generallibrary import initBases, NetworkDiagram, deco_bound_defaults, deco_cache
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
class Packager(NetworkDiagram, _PackagerMarkdown, _PackagerGitHub, _PackagerFiles, _PackagerMetadata, _PackagerPypi, _PackagerWorkflow, _PackagerRelations):
    """ Uses APIs to manage 'general' package.
        Contains methods that require more than one API as well as methods specific for ManderaGeneral.
        Todo: Allow github, pypi or local repo not to exist in any combination.
        Todo: Support writing [CI MAJOR] in msg to bump major for example. """

    LocalRepo, LocalModule, GitHub, PyPI = LocalRepo, LocalModule, GitHub, PyPI

    author = 'Rickard "Mandera" Abraham'
    email = "rickard.abraham@gmail.com"
    license = "mit"
    python = "3.8", "3.9"  # Only supports basic definition with tuple of major.minor.
    os = "windows", "ubuntu"  # , "macos"

    repos_path = ""
    github_owner = GitHub.owner
    pypi_owner = PyPI.owner

    git_exclude_lines = ".idea", "build", "dist", "*.egg-info", "__pycache__", ".git"

    @deco_bound_defaults
    def __init__(self, name, repos_path, github_owner, pypi_owner):
        self.name = name
        self.repos_path = LocalRepo.get_repos_path(path=repos_path)
        self.github_owner = github_owner
        self.pypi_owner = pypi_owner

        self.path = self.repos_path / self.name

        self._localrepo = None
        self.github = GitHub(name=self.name, owner=self.github_owner)
        self.localmodule = LocalModule(name=self.name)
        self.pypi = PyPI(name=self.name)

    def exists(self):
        """ Just check GitHub for now. """
        return GitHub(name=self.name, owner=self.owner).exists()

    @deco_cache()
    @property
    def localrepo(self):
        """ Generate, protect and cache. """
        if not self._localrepo:
            if not LocalRepo.exists(path=self.path):
                if self.github:
                    self.clone_repo(url=self.github.url, path=self.path)
                else:
                    return None
            self._localrepo = LocalRepo(path=self.path)

        return self._localrepo

    def generate_localfiles(self, aesthetic=True):
        """ Generate all local files. """
        for generate in self.files:
            if aesthetic or not generate.aesthetic:
                generate.generate()

    def __repr__(self):
        return f"<Packager: {self.name}>"


















































