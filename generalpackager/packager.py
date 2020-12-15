""" Methods specific for my general packages. """

from generallibrary import initBases, Markdown, comma_and_and
from generalfile import Path
from generalpackager import LocalRepo, LocalModule, GitHub, PyPI

import pandas
import importlib


class _PackagerMarkdown:
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

    def get_badges_markdown(self, parent=None):
        """ Get badges markdown.

            :param Packager self:
            :param parent: """
        return Markdown(*self.get_badges_list(), parent=parent)

    def get_installation_markdown(self, parent=None):
        """ Get install markdown.

            :param Packager self:
            :param parent: """
        markdown = Markdown(header="Installation", parent=parent).add_code_lines(f'pip install {self.name}')

        if len(self.metadata.extras_require) > 1:
            rows = [{
                "Name": extra,
                "Command": f"`pip install {self.name}[{extra}]`",
                "Extra packages": comma_and_and(*[f"`{x}`" for x in requires], period=False),
            } for extra, requires in self.metadata.extras_require.items()]

            Markdown(pandas.DataFrame(rows).to_markdown(index=False), header="Extras", hashtags=4, parent=markdown)

        return markdown

    def get_attributes_markdown(self, parent=None):
        """ Get attributes markdown.

            :param Packager self:
            :param parent: """
        return self.localmodule.get_attributes()


    def get_topics_markdown(self, parent=None):
        """ Get topics markdown.

            :param Packager self:
            :param parent: """
        print(self.metadata.topics)

    def get_description_markdown(self, parent=None):
        """ Get description text.

            :param Packager self:
            :param parent: """
        lines = [
            f"# Package: {self.name}",
            self.metadata.description,
        ]
        return "\n".join(lines)

    def generate_readme(self):
        """ Create readme using added APIs indirectly.

            :param Packager self: """
        markdown = Markdown()


        self.get_attributes_markdown(parent=markdown)
        # self.get_badges_markdown(parent=markdown)
        # self.get_installation_markdown(parent=markdown)

        # 2 HERE ** Expand with more methods

        print(markdown)


class _Metadata:
    name = ...
    version = ...
    description = ...
    install_requires = ...
    extras_require = ...
    classifiers = ...
    topics = ...

    def __init__(self, packager):
        self.packager = packager

        for key, value in self.packager.localrepo.get_metadata_path().read().items():
            setattr(self, key, value)

        for key in dir(self):
            if getattr(self, key) is Ellipsis:
                raise AssertionError(f"Key '{key}' for {self.packager}'s metadata is still ...")


@initBases
class Packager(_PackagerMarkdown):
    """ Uses APIs to manage 'general' package.
        Todo: Allow github, pypi or local repo not to exist in any combination. """
    def __init__(self, name, repos_path=None):
        if repos_path is None:
            repos_path = Path().absolute().parent()

        self.name = name
        self.repos_path = repos_path

        self.github = GitHub(name=name)
        self.localrepo = LocalRepo(path=repos_path / name)
        self.localmodule = LocalModule(module=importlib.import_module(name=name))
        self.pypi = PyPI(name=name)


        self.metadata = _Metadata(packager=self)

        assert self.metadata.name == self.name

    def setup_all(self):
        """ Called by GitHub Actions when a commit is pushed. """
        self.generate_readme()
        # print(self.localRepo.get_todos())
        # print(self.localRepo.get_metadata_path().read())
        # GitHub(self.localRepo.name).set_topics(["testing"])





















































