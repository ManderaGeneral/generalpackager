
from generallibrary import CodeLine, current_datetime, Markdown
from generalfile import Path
from generalpackager import LocalRepo


class _PackagerFiles:
    """ Generates setup, license and gitexclude. """
    def get_changed_files(self, aesthetic=True):
        """ Get a list of changed files compared to remote with optional aesthetic files.

            :param generalpackager.Packager self:
            :param aesthetic: """
        changed_files = []
        for relative_path in self.localrepo.get_changed_files():
            if not aesthetic and getattr({file.relative_path: file for file in self.files}.get(relative_path, None), "aesthetic", False):
                continue
            changed_files.append(relative_path)
        return changed_files

    def generate_setup(self):
        """ Generate setup.py.

            :param generalpackager.Packager self: """
        readme_path = self.localrepo.get_readme_path().relative(self.localrepo.path)
        last_version_split = self.python[-1].split(".")
        last_version_bumped_micro = f"{last_version_split[0]}.{int(last_version_split[1]) + 1}"
        setup_kwargs = {
            "name": f'"{self.localrepo.name}"',
            "author": f"'{self.author}'",
            "author_email": f'"{self.email}"',
            "version": f'"{self.localrepo.version}"',
            "description": f'"{self.localrepo.description}"',
            "long_description": f"Path(r'{readme_path}').read_text(encoding='utf-8')",
            "long_description_content_type": '"text/markdown"',
            "install_requires": self.localrepo.install_requires,
            "url": f'"{self.github.url}"',
            "license": f'"{self.license}"',
            "python_requires": f'">={self.python[0]}, <{last_version_bumped_micro}"',
            "packages": 'find_namespace_packages(exclude=("build*", "dist*"))',
            "extras_require": self.localrepo.extras_require,
            "classifiers": self.get_classifiers(),
        }

        top = CodeLine()
        top.add(CodeLine("from setuptools import setup, find_namespace_packages", space_before=1))
        top.add(CodeLine("from pathlib import Path", space_after=1))

        setup = top.add(CodeLine("setup("))
        for key, value in setup_kwargs.items():
            if isinstance(value, list) and value:
                list_ = setup.add(CodeLine(f"{key}=["))
                for item in value:
                    list_.add(CodeLine(f"'{item}',"))
                setup.add(CodeLine("],"))
            elif isinstance(value, dict) and value:
                dict_ = setup.add(CodeLine(f"{key}={{"))
                for k, v in value.items():
                    dict_.add(CodeLine(f"'{k}': {v},"))
                setup.add(CodeLine("},"))
            else:
                setup.add(CodeLine(f"{key}={value},"))

        top.add(CodeLine(")"))

        return top.text()

    def generate_git_exclude(self):
        """ Generate git exclude file.

            :param generalpackager.Packager self: """
        return "\n".join(self.git_exclude_lines)

    def generate_license(self):
        """ Generate LICENSE by using Packager.license.

            :param generalpackager.Packager self: """
        text = Path(self.repos_path / f"generalpackager/generalpackager/licenses/{self.license}").text.read()
        assert "$" in text
        text = text.replace("$year", str(current_datetime().year))
        text = text.replace("$author", self.author)
        assert "$" not in text

        return text

    def generate_workflow(self):
        """ Generate workflow.yml.

            :param generalpackager.Packager self: """
        workflow = CodeLine()
        workflow.indent_str = " " * 2

        workflow.add("name: workflow")
        workflow.add(self.get_triggers())

        jobs = workflow.add("jobs:")
        jobs.add(self.get_unittest_job())
        jobs.add(self.get_sync_and_publish_job())

        return workflow.text()

    def generate_readme(self):
        """ Generate readme markdown and overwrite README.md in local repo.

            :param generalpackager.Packager self: """
        # Description
        markdown = Markdown(self.localrepo.description, header=self.name)

        # Badges
        markdown.add_lines(*self.get_badges_dict().values())

        # Table of contents - Placeholder
        contents = Markdown(header="Contents", parent=markdown)

        # Installation
        self.get_installation_markdown().set_parent(parent=markdown)

        # Attributes
        self.get_attributes_markdown().set_parent(parent=markdown)

        # Todos
        Markdown(header="Todos", parent=markdown).add_table_lines(*self.localrepo.get_todos())

        # Table of contents - Configuration
        self.configure_contents_markdown(markdown=contents)

        # Footnote
        self.get_footnote_markdown().set_parent(parent=markdown)

        return markdown

