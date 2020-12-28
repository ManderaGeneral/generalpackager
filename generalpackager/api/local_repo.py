
from generalfile import Path
from setuptools import find_namespace_packages
import re


class LocalRepo:
    """ Tools to help Path interface a Local Python Repository. """
    def __init__(self, path):
        assert self.path_is_repo(path=path)

        self.path = Path(path).absolute()
        self.name = self.path.parts()[-1]

    def get_readme_path(self):
        """ Get a Path instance pointing to README, regardless if it exists. """
        return self.path / "README.md"

    def get_metadata_path(self):
        """ Get a Path instance pointing to README, regardless if it exists. """
        return self.path / "metadata.json"

    def get_package_paths(self):
        """ Get a list of Paths pointing to each folder containing a Python file in this local repo, aka `namespace package`. """
        return [self.path / pkg.replace(".", "/") for pkg in find_namespace_packages(where=str(self.path))]

    @classmethod
    def get_local_repos(cls, folder_path):
        """ Return a list of local repos in given folder. """
        return [path for path in Path(folder_path).get_paths_in_folder() if cls.path_is_repo(path)]

    @classmethod
    def path_is_repo(cls, path):
        """ Return whether this path is a local repo. """
        path = Path(path)
        if path.is_file():
            return False
        for file in path.get_paths_in_folder():
            if file.name() in ("metadata.json", "setup.py"):
                return True
        return False

    def get_todos(self):
        """ Get a list of dicts containing cleaned up todos.

            :rtype: dict[list[str]] """
        todos = []
        for path in self.path.get_paths_recursive():
            try:
                text = path.text.read()
            except:
                continue

            for todo in re.findall("todo+: (.+)", text, re.I):
                todos.append({
                    "Module": path.name(),
                    "Message": re.sub('[" ]*$', "", todo),
                })
        return todos








































