
from generallibrary import Markdown, comma_and_and


class _PackagerMarkdown:
    """ Contains methods to generate readme sections from arguments.
        Todo: Inherit future crawler class for pypi and github. """
    def get_badges_dict(self):
        """ Get badges as a dict.

            :param generalpackager.Packager self: """
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

            :param generalpackager.Packager self: """
        markdown = Markdown(header="Installation").add_code_lines(f'pip install {self.name}')

        if len(self.metadata.extras_require) > 1:
            list_of_dicts = [{
                "Name": extra,
                "Command": f"`pip install {self.name}[{extra}]`",
                "Extra packages": comma_and_and(*[f"`{x}`" for x in requires], period=False),
            } for extra, requires in self.metadata.extras_require.items()]

            Markdown(header="Extras", parent=markdown).add_table_lines(*list_of_dicts)

        return markdown

    def configure_contents_markdown(self, markdown):
        """ Configure table of contents lines from markdown.

            :param generalpackager.Packager self:
            :param markdown: """
        parent_markdown = markdown.get_parent(-1)
        markdown.add_pre_lines(parent_markdown.view(custom_repr=lambda md: md.link(md.header, href=True), print_out=False))
        return markdown

    def _attr_repr(self, objInfo):
        """ :param generalpackager.Packager self: """
        text = objInfo.nice_repr()
        owner = self.github.owner
        repo_name = self.name
        file_path = objInfo.module_path(repo_name=repo_name)
        line = objInfo.get_definition_line()
        commit_sha = self.commit_sha

        return Markdown.link_github_code(text=text, owner=owner, repo_name=repo_name, file_path=file_path, line=line, commit_sha=commit_sha)

    def get_attributes_markdown(self):
        """ Get a recursive view of attributes markdown.

            :param generalpackager.Packager self: """
        view_str = self.localmodule.objInfo.view(custom_repr=self._attr_repr, print_out=False)
        return Markdown(header="Attributes").add_pre_lines(view_str)

    def generate_readme(self):
        """ Generate readme markdown and overwrite README.md in local repo.
            Todo: Add footnote to readme with date and commit if specified.

            :param generalpackager.Packager self: """
        markdown = Markdown(self.metadata.description, header=self.name)
        markdown.add_table_lines(self.get_badges_dict())

        # Table of contents
        contents = Markdown(header="Contents", parent=markdown)

        # Installation
        self.get_installation_markdown().set_parent(parent=markdown)

        # Badges
        # Markdown(header="Badges", parent=markdown).add_table_lines(self.get_badges_dict())

        # Attributes
        self.get_attributes_markdown().set_parent(parent=markdown)

        # Todos
        Markdown(header="Todos", parent=markdown).add_table_lines(*self.localrepo.get_todos())

        self.configure_contents_markdown(markdown=contents)

        self.generate_file(self.localrepo.get_readme_path(), markdown)
