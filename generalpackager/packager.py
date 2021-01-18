""" Methods specific for my general packages. """

from generallibrary import initBases
from generalfile import Path
from generalpackager import LocalRepo, LocalModule, GitHub, PyPI

from generalpackager.packager_files import _PackagerFiles
from generalpackager.packager_github import _PackagerGitHub
from generalpackager.packager_markdown import _PackagerMarkdown
from generalpackager.packager_metadata import _PackagerMetadata
from generalpackager.packager_pypi import _PackagerPypi
from generalpackager.packager_workflow import _PackagerWorkflow


@initBases
class Packager(_PackagerMarkdown, _PackagerGitHub, _PackagerFiles, _PackagerMetadata, _PackagerPypi, _PackagerWorkflow):
    """ Uses APIs to manage 'general' package.
        Contains methods that require more than one API as well as methods specific for ManderaGeneral.
        Todo: Allow github, pypi or local repo not to exist in any combination. """

    author = 'Rickard "Mandera" Abraham'
    email = "rickard.abraham@gmail.com"
    license = "mit"
    python = "3.8", "3.9"  # Only supports basic definition with tuple of major.minor
    os = "windows", "ubuntu"
    # os = "windows", "macos", "ubuntu"

    git_exclude_lines = ".idea", "build", "dist", "*.egg-info", "__pycache__", ".git"

    def __init__(self, name, repos_path=None, commit_sha="master"):
        if repos_path is None:
            repos_path = Path(repos_path).absolute()
            while not LocalRepo.get_local_repos(repos_path):
                repos_path = repos_path.get_parent()
                if repos_path is None:
                    raise AttributeError(f"Couldn't find repos path.")

        # print(repos_path)
        # print("Repo path view:")
        # list(repos_path.get_paths_recursive(depth=4))
        # repos_path.view()

        self.name = name
        self.repos_path = repos_path
        self.commit_sha = commit_sha

        self.path = self.repos_path / self.name

        self._localrepo = None
        self._github = None
        self._localmodule = None
        self._pypi = None

        # assert self.localrepo.name == self.name

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




    @staticmethod
    def get_users_packages(pypi_user=None, github_user=None):
        """ Return a set of user's packages with intersecting PyPI and GitHub. """
        return PyPI.get_users_packages(user=pypi_user).intersection(GitHub.get_users_packages(user=github_user))

    def generate_localfiles(self):
        """ Generate all local files. """
        self.generate_git_exclude()
        self.generate_readme()
        self.generate_setup()
        self.generate_license()
        self.generate_workflow()

    def sync_package(self, message=None):
        """ Called by GitHub Actions when a commit is pushed. """
        self.generate_localfiles()
        self.sync_github_metadata()
        self.localrepo.commit_and_push(message=message)

    def __repr__(self):
        return f"<Packager: {self.name}>"























































