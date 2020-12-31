""" Methods specific for my general packages. """

from generallibrary import initBases
from generalfile import Path
from generalpackager import LocalRepo, LocalModule, GitHub, PyPI

from generalpackager.metadata import _Metadata
from generalpackager.packager_files import _PackagerFiles
from generalpackager.packager_github import _PackagerGitHub
from generalpackager.packager_markdown import _PackagerMarkdown

import importlib


@initBases
class Packager(_PackagerMarkdown, _PackagerGitHub, _PackagerFiles):
    """ Uses APIs to manage 'general' package.
        Contains methods that require more than one API as well as methods specific for ManderaGeneral.
        Todo: Allow github, pypi or local repo not to exist in any combination. """

    author = 'Rickard "Mandera" Abraham'
    license = "mit-license"
    python = "3.8", "3.9"
    os = "windows", "macos", "linux"

    git_exclude_lines = "/.idea/",

    def __init__(self, name, repos_path=None, commit_sha="master"):
        if repos_path is None:
            repos_path = Path().absolute().get_parent()

        self.name = name
        self.repos_path = repos_path
        self.commit_sha = commit_sha

        self.github = GitHub(name=name)
        self.localrepo = LocalRepo(path=repos_path / name)
        self.localmodule = LocalModule(module=importlib.import_module(name=name))
        self.pypi = PyPI(name=name)

        self.metadata = _Metadata(packager=self)

        assert self.metadata.name == self.name

    def setup_all(self):
        """ Called by GitHub Actions when a commit is pushed.
            Todo: Generate a release history from commit history.
            Todo: Generate setup_template.py """
        # self.generate_git_exclude()
        # self.generate_readme()
        # self.localrepo.commit_and_push()
        # self.sync_github_metadata()
        self.generate_setup()

























































