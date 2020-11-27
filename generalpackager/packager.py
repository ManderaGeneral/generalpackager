

from generallibrary import initBases, Markdown, comma_and_and
from generalfile import Path
from generalpackager import LocalRepo

import pandas


class _Readme:
    """ Contains methods to generate readme sections from arguments. """

    def get_badges_list(self):
        """ Get badges list.

            :param Packager self: """
        pypi_version = "[![PyPI version shields.io](https://img.shields.io/pypi/v/PACKAGE.svg)](https://pypi.org/project/PACKAGE/)"
        python_version = "[![PyPI pyversions](https://img.shields.io/pypi/pyversions/PACKAGE.svg)](https://pypi.python.org/pypi/PACKAGE/)"
        platforms = "[![Generic badge](https://img.shields.io/badge/platforms-Windows%20|%20Ubuntu%20|%20MacOS-blue.svg)](https://shields.io/)"
        workflow = "[![workflow Actions Status](https://github.com/ManderaGeneral/PACKAGE/workflows/workflow/badge.svg)](https://github.com/ManderaGeneral/PACKAGE/actions)"
        lgtm_alerts = "[![Total alerts](https://img.shields.io/lgtm/alerts/g/ManderaGeneral/PACKAGE.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ManderaGeneral/PACKAGE/alerts/)"

        return [badge.replace("PACKAGE", self.name) for badge in (pypi_version, python_version, platforms, workflow, lgtm_alerts)]

    def get_badges_markdown(self):
        """ Get badges markdown.

            :param Packager self: """
        return Markdown(*self.get_badges_list())

    def get_installation_markdown(self, name, extras_require):
        """ Get install markdown.

            :param Packager self: """
        markdown = Markdown(header="Installation").add_code_lines(f'pip install {name}')

        if len(extras_require) > 1:
            rows = [{
                "Name": extra,
                "Command": f"`pip install {name}[{extra}]`",
                "Extra packages": comma_and_and(*[f"`{x}`" for x in requires], period=False),
            } for extra, requires in extras_require.items()]

            Markdown(pandas.DataFrame(rows).to_markdown(index=False), header="Extras", hashtags=4, parent=markdown)

        return markdown

    def get_topics_markdown(self, topics):
        """ Get topics markdown.

            :param Packager self: """
        print(topics)

    def get_description_markdown(self, name, description):
        """ Get description text.

            :param Packager self: """

        lines = [
            f"# Package: {name}",
            description,
        ]
        return "\n".join(lines)


    def generate_readme(self):
        """ Create readme using added APIs indirectly.

            :param Packager self: """
        l = [
            self.get_badges_markdown(),
            self.get_installation_markdown(),
        ]

        markdown = Markdown()
        for md in l:
            md.set_parent(markdown)
        print(markdown)


class _Metadata:
    name, version, description, install_requires, extras_require, classifiers = ..., ..., ..., ..., ..., ...
    def __init__(self, packager):
        self.packager = packager
        # HERE ** Load metadata values into here, then use through readme methods above

@initBases
class Packager(_Readme):
    """ Uses APIs to manage 'general' package. """
    def __init__(self, repo_path=None):
        self.repo_path = None if repo_path is None else Path(repo_path)

        # One of the options to get localRepo
        self.localRepo = LocalRepo(self.repo_path)

        self.metadata = _Metadata(packager=self)
