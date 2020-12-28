""" Methods specific for my general packages. """

from generallibrary import initBases, Markdown, comma_and_and
from generalfile import Path
from generalpackager import LocalRepo, LocalModule, GitHub, PyPI

import importlib


class _PackagerMarkdown:
    """ Contains methods to generate readme sections from arguments.
        Todo: Inherit future crawler class for pypi and github. """
    def get_badges_dict(self):
        """ Get badges as a dict.

            :param Packager self: """
        badges = {
            "UnitTests": "[![workflow Actions Status](https://github.com/ManderaGeneral/PACKAGE/workflows/workflow/badge.svg)](https://github.com/ManderaGeneral/PACKAGE/actions)",
            "Alerts": "[![Total alerts](https://img.shields.io/lgtm/alerts/g/ManderaGeneral/PACKAGE.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ManderaGeneral/PACKAGE/alerts/)",
            "Commit": "![GitHub last commit](https://img.shields.io/github/last-commit/ManderaGeneral/PACKAGE)",
            "Release": "[![PyPI version shields.io](https://img.shields.io/pypi/v/PACKAGE.svg)](https://pypi.org/project/PACKAGE/)",
            "Python": "[![PyPI pyversions](https://img.shields.io/pypi/pyversions/PACKAGE.svg)](https://pypi.python.org/pypi/PACKAGE/)",
            "Operating System": "[![Generic badge](https://img.shields.io/badge/platforms-Windows%20%7C%20Ubuntu%20%7C%20MacOS-blue.svg)](https://shields.io/)",
        }
        return {key: value.replace("PACKAGE", self.name) for key, value in badges.items()}

    def get_installation_markdown(self):
        """ Get install markdown.

            :param Packager self: """
        markdown = Markdown(header="Installation").add_code_lines(f'pip install {self.name}')

        if len(self.metadata.extras_require) > 1:
            list_of_dicts = [{
                "Name": extra,
                "Command": f"`pip install {self.name}[{extra}]`",
                "Extra packages": comma_and_and(*[f"`{x}`" for x in requires], period=False),
            } for extra, requires in self.metadata.extras_require.items()]

            Markdown(header="Extras", parent=markdown).add_table_lines(*list_of_dicts)

        return markdown

    def get_table_of_contents_markdown(self, parent_markdown):
        """ Get table of contents lines.

            :param Packager self:
            :param parent_markdown: """
        markdown = Markdown(parent_markdown.view(custom_repr=lambda md: md.link(md.header, href=True), print_out=False).replace("\n", "  \n"))
        markdown.wrap_with_tags("pre")
        return markdown



    def generate_readme(self):
        """ Create readme markdown object.

            :param Packager self: """
        markdown = Markdown(header=self.name)

        # Description
        Markdown(self.metadata.description, header="Description", parent=markdown)

        # Badges
        Markdown(header="Badges", parent=markdown).add_table_lines(self.get_badges_dict())

        # Installation
        self.get_installation_markdown().set_parent(parent=markdown)

        # Todos
        Markdown(header="Todos", parent=markdown).add_table_lines(*self.localrepo.get_todos())

        # Attributes
        self.localmodule.get_attributes_markdown().set_parent(parent=markdown)

        # Table of contents
        self.get_table_of_contents_markdown(parent_markdown=markdown).set_parent(parent=markdown).set_index(0)
        # Markdown().add_code_lines(*self.get_table_of_contents(markdown)).set_parent(parent=markdown).set_index(0)
        # Markdown(*self.get_table_of_contents(markdown)).set_parent(parent=markdown).set_index(0)

        return markdown

    def sync_github_metadata(self):
        """ Sync GitHub with local metadata.

            :param Packager self: """
        self.github.set_website(f"https://pypi.org/project/{self.name}/")
        self.github.set_description(self.metadata.description)
        self.github.set_topics(self.metadata.topics)



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
            repos_path = Path().absolute().get_parent()

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
        self.localrepo.get_readme_path().text.write(self.generate_readme(), overwrite=True)
        # self.commit_and_push()

        # self.sync_github_metadata()

        # HERE ** TOC links
        # 2 HERE ** Release history from commits
        # 3 HERE ** Generate classifiers from topics























































