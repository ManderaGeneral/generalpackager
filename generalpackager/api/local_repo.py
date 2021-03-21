
from generalfile import Path
from generalpackager import GIT_PASSWORD
from generallibrary import Ver, deco_cache, Recycle

from setuptools import find_namespace_packages
import re
from git import Repo
import subprocess
import sys


def load_metadata_before(func):
    def _wrapper(self, *args, **kwargs):
        """ :param LocalRepo self: """
        if not self.has_loaded_metadata:
            self.load_metadata()
        return func(self, *args, **kwargs)
    return _wrapper


class LocalRepo(Recycle):
    """ Tools to help Path interface a Local Python Repository.
        Todo: Search for imports to list dependencies. """
    enabled = True
    name = ...
    version = "0.0.1"  # type: Ver
    description = "Missing description."
    install_requires = []
    extras_require = {}
    topics = []
    manifest = []

    metadata_keys = [key for key, value in locals().items() if not key.startswith("_")]
    _recycle_keys = {"path": lambda path: str(LocalRepo.scrub_path(path=path))}

    def __init__(self, path=None):
        self.path = self.scrub_path(path=path)
        self.has_loaded_metadata = False

    def __repr__(self):
        return str(self.path)

    def has_metadata(self):
        return self.get_metadata_path().exists()

    def load_metadata(self):
        for key, value in self.get_metadata_path().read().items():
            setattr(self, f"_{key}", value)

        if self.extras_require:
            self.extras_require["full"] = list(set().union(*self.extras_require.values()))
            self.extras_require["full"].sort()

        self.version = Ver(self.version)

        if self.name is Ellipsis:
            self.name = self.path.name()

        self.has_loaded_metadata = True

    def exists(self):
        """ Return whether this API's target exists. """
        self.path_exists(path=self.path)

    @classmethod
    def path_exists(self, path):
        if path.is_file() or not path.exists():
            return False
        return bool(path.get_child(filt=lambda x: x.name() == ".git"))

    @classmethod
    def get_first_repo(cls, path=None):
        """ Return first found LocalRepo that can be created or None.

            :param generalfile.Path or any path:
            :rtype: generalfile.Path """
        path = cls.get_first_repo_path(path=path)
        return None if path is None else LocalRepo(path=path)

    @classmethod
    def get_first_repo_path(cls, path=None):
        """ Return first found Path where LocalRepo can be created or None.

            :param generalfile.Path or any path:
            :rtype: generalfile.Path """
        return Path(path=path).absolute().get_parent(depth=-1, include_self=True, filt=lambda path: LocalRepo.path_exists(path=path))

    @classmethod
    def scrub_path(cls, path=None):
        """ Scrub path.

            :param generalfile.Path or any path:
            :rtype: generalfile.Path """
        return cls.get_first_repo_path(path=path) or Path(path).absolute()

    @classmethod
    def get_local_repos(cls, folder_path):
        """ Return a list of local repo paths in given folder. """
        return [local_repo for path in Path(folder_path).get_children() if (local_repo := LocalRepo(path=path)).exists()]

    @staticmethod
    def get_repos_path(path=None):
        """ Try to return absolute path pointing to folder containing repos by searching parents. """
        return Path(path).absolute().get_parent(depth=-1, include_self=True, filt=lambda path: LocalRepo.get_local_repos(path))

    @load_metadata_before
    def metadata_getter(self, key):
        return getattr(self, f"_{key}")

    @load_metadata_before
    def metadata_setter(self, key, value):
        """ Set a metadata's key both in instance and json file. """
        if self.has_metadata() and value != getattr(self, f"_{key}", ...):
            metadata = self.get_metadata_path().read()
            metadata[key] = str(value)
            self.get_metadata_path().write(metadata, overwrite=True, indent=4)
        setattr(self, f"_{key}", value)

    def get_readme_path(self):
        """ Get a Path instance pointing to README.md, regardless if it exists. """
        return self.path / "README.md"

    def get_metadata_path(self):
        """ Get a Path instance pointing to metadata.json, regardless if it exists. """
        return self.path / "metadata.json"

    def get_git_exclude_path(self):
        """ Get a Path instance pointing to .git/info/exclude, regardless if it exists. """
        return self.path / ".git/info/exclude"

    def get_setup_path(self):
        """ Get a Path instance pointing to setup.py, regardless if it exists. """
        return self.path / "setup.py"

    def get_manifest_path(self):
        """ Get a Path instance pointing to MANIFEST.in, regardless if it exists. """
        return self.path / "MANIFEST.in"

    def get_license_path(self):
        """ Get a Path instance pointing to LICENSE, regardless if it exists. """
        return self.path / "LICENSE"

    def get_workflow_path(self):
        """ Get a Path instance pointing to workflow.yml, regardless if it exists. """
        return self.path / ".github/workflows/workflow.yml"

    def get_test_path(self):
        """ Get a Path instance pointing to workflow.yml, regardless if it exists. """
        return self.path / f"{self.name}/test"

    @deco_cache()
    def get_test_paths(self):
        """ Get a list of paths to each test python file. """
        return self.get_test_path().get_children(depth=-1, filt=lambda path: path.match("*.py"))

    @deco_cache()
    def text_in_tests(self, text):
        """ Return whether text exists in one of the test files. """
        for path in self.get_test_paths():
            if path.contains(text=text):
                return True
        return False

    def get_package_paths(self):
        """ Get a list of Paths pointing to each folder containing a Python file in this local repo, aka `namespace package`. """
        return [self.path / pkg.replace(".", "/") for pkg in find_namespace_packages(where=str(self.path))]

    def commit_and_push(self, message=None, tag=False, owner=None):
        """ Commit and push this local repo to GitHub.
            Return short sha1 of pushed commit. """
        if message is None:
            message = "Automatic commit."
        if owner is None:
            owner = "ManderaGeneral"

        repo = Repo(str(self.path))

        repo.git.add(A=True)
        repo.index.commit(message=str(message))
        remote = repo.remote()
        remote.set_url(f"https://Mandera:{GIT_PASSWORD}@github.com/{owner}/{self.name}.git")

        if tag:
            tag_ref = repo.create_tag(f"v{self.version}", force=True)
            remote.push(refspec=tag_ref)

        return remote.push()[0].summary.split("..")[1].rstrip()

    def get_changed_files(self):
        """ Get a list of changed files compared to remote. """
        repo = Repo(str(self.path))
        return re.findall("diff --git a/(.*) " + "b/", repo.git.diff())

    def bump_version(self):
        """ Bump micro version in metadata.json. """
        self.version = self.version.bump()

    def pip_install(self):
        """ Install this repository with pip, WITHOUT -e flag.
            Subprocess messed up -e flag compared to doing it in terminal, so use the normal one."""
        subprocess.check_call([sys.executable, "-m", "pip", "install", str(self.path)])

    def unittest(self):
        """ Run unittests for this repository. """
        subprocess.check_call([sys.executable, "-m", "unittest", "discover", str(self.get_test_path())])

    def create_sdist(self):
        """ Create source distribution. """
        with self.path.as_working_dir():
            subprocess.check_call([sys.executable, "setup.py", "sdist", "bdist_wheel"])

    def upload(self):
        """ Upload local repo to PyPI. """
        self.create_sdist()
        with self.path.as_working_dir():
            subprocess.check_call([sys.executable, "-m", "twine", "upload", "dist/*"])

for key in LocalRepo.metadata_keys:
    value = getattr(LocalRepo, key)
    setattr(LocalRepo, f"_{key}", value)
    setattr(LocalRepo, key, property(
        fget=lambda self, key=key: LocalRepo.metadata_getter(self, key),
        fset=lambda self, value, key=key: LocalRepo.metadata_setter(self, key, value),
    ))


































