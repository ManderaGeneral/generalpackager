
from generalfile import Path
from setuptools import find_namespace_packages


class LocalRepo:
    """ Tools to help Path interface a Local Python Repository. """
    def __init__(self, repo_root):
        self.repo_root = Path(repo_root).absolute()

    def get_readme_path(self):
        """ Get a Path instance pointing to README, regardless if it exists. """
        return self.repo_root / "README.md"

    def get_metadata_path(self):
        """ Get a Path instance pointing to README, regardless if it exists. """
        return self.repo_root / "metadata.json"

    def get_package_paths(self):
        """ Get a list of Paths pointing to each folder containing a Python file, aka `namespace package`. """
        return [self.repo_root / pkg.replace(".", "/") for pkg in find_namespace_packages(where=str(self.repo_root))]


