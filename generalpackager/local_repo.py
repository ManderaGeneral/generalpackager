""" generalpackager will work on many levels, this level will be 'cloned repository level'.

    Planned modules:
        - Barren
        - Local repository
        - PyPI
        - GitHub

    Planned features:
        - Create new empty repository with template.
        - Dry README for packages and my profile, directly updated.
        - Register a package on PyPI.
        - Update GitHub package info.

    Read: https://guides.github.com/features/wikis/

    - Todo: Read commit message history to create `Releases`.
    - Todo: See if we can generate readme before local commit.
    - Todo: Publish this packages.
    - Todo: Make GitHub actions use this package with `shared` repo.
    """
from generalfile import Path
from generallibrary import attributes_to_markdown, comma_and_and, addToListInDict, remove_duplicates, TreeDiagram, initBases
import pandas
import sys
import re
from itertools import chain
import requests
import os
import json


# Current: setup.py runs code to fill info during runtime
# Goal: setup.py is generated in GitHub actions by `shared` using `generalpackager` so that it is static during runtime

class Barren:
    """ Contains methods that don't require repository or installed packages. """
    @staticmethod
    def get_badges(name):
        """ Get badge image urls text. """
        pypi_version = "[![PyPI version shields.io](https://img.shields.io/pypi/v/PACKAGE.svg)](https://pypi.org/project/PACKAGE/)"
        python_version = "[![PyPI pyversions](https://img.shields.io/pypi/pyversions/PACKAGE.svg)](https://pypi.python.org/pypi/PACKAGE/)"
        platforms = "[![Generic badge](https://img.shields.io/badge/platforms-Windows%20|%20Ubuntu%20|%20MacOS-blue.svg)](https://shields.io/)"
        workflow = "[![workflow Actions Status](https://github.com/ManderaGeneral/PACKAGE/workflows/workflow/badge.svg)](https://github.com/ManderaGeneral/PACKAGE/actions)"
        lgtm_alerts = "[![Total alerts](https://img.shields.io/lgtm/alerts/g/ManderaGeneral/PACKAGE.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ManderaGeneral/PACKAGE/alerts/)"

        return "\n".join([
            pypi_version,
            python_version,
            platforms,
            workflow,
            lgtm_alerts,
        ]).replace("PACKAGE", name)



@initBases
class Markdown(TreeDiagram):
    """ Section for a markdown file, contains all MD specific methods. """
    def __init__(self, header=None, *lines, hashtags=None, parent=None):
        if hashtags is None:
            hashtags = 2

        self.header = header
        self.lines = lines
        self.hashtags = hashtags

    def section_lines(self):
        """ Get a list of all lines in this section. """
        lines = list(self.lines)
        if self.header:
            lines.insert(0, f"{'#' * self.hashtags} {self.header}")
        return lines

    def all_lines(self):
        """ Get a list of all lines in this entire Markdown by iterating all children. """
        lines = self.section_lines()

        for markdown in self.get_all():
            lines.extend(markdown.section_lines())  # HERE ** Try this, see if we can put extra newline between sections

        return lines

    def add(self, part):
        """ Add a part to this markdown"""
        self.parts.append(part)

    def add_code(self, header, *lines, hashtags=None):
        """ Add a code part. """
        Markdown(header, "```", *lines, "```", hashtags=hashtags, parent=self)

    def __str__(self):
        return '\n'.join(self.all_lines())


class GitHub:
    """ All GitHub specific methods. """
    headers = {
        "Accept": "application/vnd.github.mercy-preview+json",
        # "Authorization": f"token {os.environ['packager_github_api']}",
    }
    token = os.environ['packager_github_api']
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name

    def get_topics(self):
        """ Fetch topics as a list. """
        return requests.get(f"https://api.github.com/repos/{self.owner}/{self.name}/topics", headers=self.headers).json().get("names")

    def set_topics(self, topics):
        """ Send a request to change topics. """
        url = f"https://api.github.com/repos/{self.owner}/{self.name}/topics"
        data = json.dumps({"names": topics})
        return requests.put(url, auth=(self.owner, self.token), headers=self.headers, data=data)



class LocalRepo:
    """ All markdown specific repository methods. """
    name, version, description, install_requires, extras_require, classifiers = ..., ..., ..., ..., ..., ...
    def __init__(self, repo_root):
        self.repo_root = Path(repo_root).absolute()

        self._load_package_specific()

        # Todo: Update `topics` in PS with shareds'. Not sure if we do that in `packager` or `shared` yet.
        self.extras_require["full"] = remove_duplicates([package for package in chain(*list(self.extras_require.values()))])

    def _load_package_specific(self):
        ps = (self.repo_root / "package_specific.json").read()
        for key, value in ps.items():
            setattr(self, key, value)
        for key, value in LocalRepo.__dict__.items():
            if value is ... and getattr(self, key) is ...:
                raise AssertionError(f"{key} isn't defined")


    def get_install_section(self):
        """ Get install text. """
        section = Markdown()

        lines = [
            f"## Installation",
            "```",
            f'pip install {self.name}',
            "```",
        ]

        if len(self.extras_require) > 1:
            rows = [{
                "Name": extra,
                "Command": f"`pip install {self.name}[{extra}]`",
                "Extra packages": comma_and_and(*[f"`{x}`" for x in requires], period=False),
            } for extra, requires in self.extras_require.items()]

            df = pandas.DataFrame(rows)
            lines.extend(["#### Extras", df.to_markdown(index=False)])


        return "\n".join(lines)

    def get_description(self):
        """ Get description text. """
        lines = [
            f"# Package: {self.name}",
            self.description,
        ]
        return "\n".join(lines)

    def get_badges(self):
        """ Redirect to `Barren.get_badges`. """
        return Barren.get_badges(self.name)

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
