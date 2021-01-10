
from generallibrary import CodeLine, current_datetime
from generalfile import Path


class _PackagerFiles:
    """ Generates setup, license and gitexclude. """
    def generate_file(self, path, text):
        """ Overwrite a file in local repo with generated text.

            :param generalpackager.Packager self:
            :param path:
            :param text: """
        path.text.write(text, overwrite=True)

    def generate_test_main(self):
        """ Generate test/main.py.

            :param generalpackager.Packager self: """
        main = CodeLine()
        main.add("import unittest", 1)
        main.add("from generallibrary import get_launch_options, EnvVar", 1)
        loop = main.add("for key, value in get_launch_options().items():", 2)
        loop.add("EnvVar(name=key).value = value")
        main.add('unittest.TextTestRunner().run(unittest.TestLoader().discover("generalpackager/test"))', 1, 1)

        self.generate_file(self.localrepo.get_test_main_path(), main)

    def generate_setup(self):
        """ Generate setup.py.

            :param generalpackager.Packager self: """
        last_version_split = self.python[-1].split(".")
        last_version_bumped_micro = f"{last_version_split[0]}.{int(last_version_split[1]) + 1}"
        setup_kwargs = {
            "name": f'"{self.localrepo.name}"',
            "author": f"'{self.author}'",
            "author_email": f'"{self.email}"',
            "version": f'"{self.localrepo.version}"',
            "description": f'"{self.localrepo.description}"',
            "long_description": f"Path(r'{self.localrepo.get_readme_path().relative()}').read_text(encoding='utf-8')",
            "long_description_content_type": '"text/markdown"',
            "install_requires": self.localrepo.install_requires,
            "url": f'"{self.github.url()}"',
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
            if isinstance(value, list):
                list_ = setup.add(CodeLine(f"{key}=["))
                for item in value:
                    list_.add(CodeLine(f"'{item}',"))
                setup.add(CodeLine("],"))
            else:
                setup.add(CodeLine(f"{key}={value},"))

        top.add(CodeLine(")", space_after=1))

        self.generate_file(self.localrepo.get_setup_path(), top.text())

    def generate_git_exclude(self):
        """ Generate git exclude file.

            :param generalpackager.Packager self: """
        self.generate_file(self.localrepo.get_git_exclude_path(), "\n".join(self.git_exclude_lines))

    def generate_license(self):
        """ Generate LICENSE by using Packager.license.

            :param generalpackager.Packager self: """
        text = Path(self.repos_path / f"generalpackager/generalpackager/licenses/{self.license}").text.read()
        assert "$" in text
        text = text.replace("$year", str(current_datetime().year))
        text = text.replace("$author", self.author)
        assert "$" not in text

        self.generate_file(self.localrepo.get_license_path(), text)

    def generate_workflow(self):
        """ Generate workflow.yml.

            :param generalpackager.Packager self: """
        workflow = CodeLine()
        workflow.indent_str = " " * 2

        workflow.add("name: workflow")
        workflow.add(self.get_triggers())

        jobs = workflow.add("jobs:")
        jobs.add(self.get_unittest_job())

        self.localrepo.get_workflow_path().text.write(workflow.text(), overwrite=True)
