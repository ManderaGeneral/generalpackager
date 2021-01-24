""" Methods specific for my general packages.
    Isolatable methods are put inside APIs. """

from generallibrary import initBases, NetworkDiagram
from generalpackager import LocalRepo, LocalModule, GitHub, PyPI

from generalpackager.packager_files import _PackagerFiles
from generalpackager.packager_github import _PackagerGitHub
from generalpackager.packager_markdown import _PackagerMarkdown
from generalpackager.packager_metadata import _PackagerMetadata
from generalpackager.packager_pypi import _PackagerPypi
from generalpackager.packager_workflow import _PackagerWorkflow


@initBases
class Packager(NetworkDiagram, _PackagerMarkdown, _PackagerGitHub, _PackagerFiles, _PackagerMetadata, _PackagerPypi, _PackagerWorkflow):
    """ Uses APIs to manage 'general' package.
        Contains methods that require more than one API as well as methods specific for ManderaGeneral.
        Todo: Allow github, pypi or local repo not to exist in any combination.
        Todo: Replace badges with generated hardcode. """

    author = 'Rickard "Mandera" Abraham'
    email = "rickard.abraham@gmail.com"
    license = "mit"
    python = "3.8", "3.9"  # Only supports basic definition with tuple of major.minor
    os = "windows", "ubuntu"  # , "macos"

    git_exclude_lines = ".idea", "build", "dist", "*.egg-info", "__pycache__", ".git"

    def __init__(self, name, repos_path=None, commit_sha="master"):
        self.name = name
        self.repos_path = LocalRepo.get_repos_path(path=repos_path)
        self.commit_sha = commit_sha

        self.path = self.repos_path / self.name

        self._localrepo = None
        self._github = None
        self._localmodule = None
        self._pypi = None

    @staticmethod
    def is_creatable(name):
        """ Simple placeholder check. """
        return GitHub.is_creatable(name=name, owner="ManderaGeneral")

    @property
    def localrepo(self):
        """ Generate, protect and cache. """
        if not self._localrepo:
            if not LocalRepo.is_creatable(path=self.path):
                if self.github:
                    self.clone_repo(url=self.github.url, path=self.path)
                else:
                    return None
            self._localrepo = LocalRepo(path=self.path, git_exclude_lines=self.git_exclude_lines)

        return self._localrepo

    @property
    def github(self):
        """ Generate, protect and cache. """
        if not self._github:
            self._github = GitHub(name=self.name)

        return self._github

    @property
    def localmodule(self):
        """ Generate, protect and cache. """
        if not self._localmodule:
            self._localmodule = LocalModule(name=self.name)

        return self._localmodule

    @property
    def pypi(self):
        """ Generate, protect and cache. """
        if not self._pypi:
            self._pypi = PyPI(name=self.name)
        return self._pypi

    def get_packagers_dict(self):
        """ Get a dict of Packagers connected to this one using name as key. """
        return {packager.name: packager for packager in self.get_routes().get_nodes()}

    def get_packager_with_name(self, name):
        """ Return Packager or None. """
        packager = self.get_packagers_dict().get(name)
        if packager is None and Packager.is_creatable(name=name):
            packager = Packager(name=name, repos_path=self.repos_path)
        return packager

    def load_general_packagers(self):
        for name in Packager.get_users_package_names():
            packager = self.get_packager_with_name(name=name)
            for dependency_name in packager.localrepo.install_requires:
                dependency_packager = self.get_packager_with_name(name=dependency_name)
                if dependency_packager is not None:
                    dependency_packager.link(target=packager)

    @staticmethod
    def get_users_package_names(pypi_user=None, github_user=None):
        """ Return a set of user's packages with intersecting PyPI and GitHub. """
        return PyPI.get_users_packages(user=pypi_user).intersection(GitHub.get_users_packages(user=github_user))

    def generate_localfiles(self, generate_aesthetic=True):
        """ Generate all local files. """
        for generate in self.files:
            if generate_aesthetic or not generate.aesthetic:
                generate.generate()

    def sync_package(self, message=None):
        """ Called by GitHub Actions when a commit is pushed. """
        self.generate_localfiles()
        self.sync_github_metadata()
        self.localrepo.commit_and_push(message=message)

    def __repr__(self):
        return f"<Packager: {self.name}>"


















































