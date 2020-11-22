""" generalpackager will work on many levels, this level will be 'cloned repository level'. """
from generalfile import Path
import importlib
from generallibrary import attributes_to_markdown, remove_duplicates, comma_and_and
from itertools import chain
import pandas

import sys


# Current: setup.py runs code to fill info during runtime
# Goal: setup.py is generated in GitHub actions by `shared` using `generalpackager` so that it is static during runtime


class RepoMarkdown:
    """ All markdown specific repository methods. """
    name, version, description, install_requires, extras_require, full, classifiers = ..., ..., ..., ..., ..., ..., ...
    def __init__(self, repo_root):
        self.repo_root = Path(repo_root).absolute()

        ps = Path("package_specific.json").read()
        for key, value in ps.items():
            setattr(self, key, value)

    def get_badges(self):
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
        ]).replace("PACKAGE", self.name)
        # ]).replace("PACKAGE", "generallibrary")

    def get_install(self):
        """ Get install text. """
        lines = [
            f"## Installation",
            "```",
            f'pip install {self.name}',
            "```",
        ]

        if len(self.extras_require) > 1:
            rows = [{
                "Name": extra,
                "Installation": f"`pip install {self.name}[{extra}]`",
                "Packages": comma_and_and(*requires, period=False),
            } for extra, requires in self.extras_require.items()]

            df = pandas.DataFrame(rows)
            lines.extend(["#### Extras", df.to_markdown(index=False)])


        return "\n".join(lines)

    def get_attributes(self):
        """ Get attributes text. """
        return attributes_to_markdown(sys.modules[self.name], print_out=False, return_lines=False)




    def create_readme(self, content):
        """ Create README. """
        readme = self.repo_root / "README.md"
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