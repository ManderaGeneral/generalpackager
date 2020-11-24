""" generalpackager will work on many levels, this level will be 'cloned repository level'.

    Planned modules:
        - Barren
        - Local repository
        - PyPI
        - APIGitHub

    Planned features:
        - Create new empty repository with template.
        - Dry README for packages and my profile, directly updated.
        - Register a package on PyPI.
        - Update APIGitHub package info.

    Read: https://guides.github.com/features/wikis/

    - Todo: Read commit message history to create `Releases`.
    - Todo: See if we can generate readme before local commit.
    - Todo: Publish this packages.
    - Todo: Make APIGitHub actions use this package with `shared` repo.
    - Todo: Generate setup.py
    """
from generalfile import Path
from generallibrary import attributes_to_markdown, addToListInDict, remove_duplicates
import sys
import re
from itertools import chain


class APILocalRepo:
    """ All markdown specific repository methods.
        Todo: Update `topics` in PS with shareds'. Not sure if we do that in `packager` or `shared` yet. """
    name, version, description, install_requires, extras_require, classifiers = ..., ..., ..., ..., ..., ...
    fetched_keys = [key for key in locals() if not key.startswith("_")]

    def _load_package_specific(self):
        ps = (self.repo_root / "package_specific.json").read()
        for key in self.fetched_keys:
            setattr(self, key, ps[key])
        self.extras_require["full"] = remove_duplicates([package for package in chain(*list(self.extras_require.values()))])

    def __init__(self, repo_root):
        self.repo_root = Path(repo_root).absolute()
        self._load_package_specific()

    def get_description(self):
        """ Get description text. """
        lines = [
            f"# Package: {self.name}",
            self.description,
        ]
        return "\n".join(lines)

    def get_attributes(self):
        """ Get attributes text. """
        return attributes_to_markdown(sys.modules[self.name], print_out=False, return_lines=False)

    def get_todos(self):
        """ Search package files for to do comments. """
        base_path = self.repo_root / self.name
        todos = {}
        for path in base_path.get_paths_recursive(include_folders=False):
            if "_" in path and "__init__" not in path:
                continue
            module = path.remove_start(base_path)
            for todo in re.findall("todo+: (.+)", path.text.read(), re.I):
                filtered_todo = re.sub('[" ]*$', "", todo)
                addToListInDict(todos, module, filtered_todo)

        if todos:
            lines = ["## Todo"]
            for module, todos in todos.items():
                lines.append(f" - `{module}`")
                lines.extend([f"   - {todo}" for todo in todos])

            return "\n".join(lines)


    def create_readme(self, content):
        """ Create README. """
        readme = self.repo_root / "README.md"
        content = [x for x in content if x]
        readme.text.write("\n\n".join(content), overwrite=True)








    # def import_package_specific(self):
    #     """ Dynamically import package specific dictionary.
    #
    #         :rtype: dict """
    #     ps = getattr(importlib.import_module("package_specific", package=f".{self.repo_name}"), "ps")
    #
    #     ps["extras_require"]["full"] = remove_duplicates([package for package in chain(*list(ps["extras_require"].values()))])
    #
    #     return ps
