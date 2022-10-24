
import json

from generalfile import Path
from generallibrary import CodeLine, Markdown, Date, deco_cache, Timer, Log


class _PackagerFiles:
    @classmethod
    def create_blank_locally_python(cls, path, install=True):
        """ Create a new general package locally only.
            Todo: Fix create_blank, it overwrites current projects pip install.

            :param generalpackager.Packager or Any cls:
            :param Path or str path:
            :param install: Whether to pip install. """
        path = Path(path)
        assert path.empty()
        packager = cls(name=path.name(), path=path, target=cls.Targets.python)

        packager.localrepo.metadata.write_config()
        packager.generate_localfiles()

        if install:
            packager.localrepo.pip_install_editable()

        # new_self = packager.get_new_packager()  # Reset caches to get updated files
        # new_self.generate_localfiles()

        return packager


    @deco_cache()
    def _compare_local(self, platform, aesthetic):
        """ :param generalpackager.Packager self: """
        def filt(path):
            if path.match(*self.git_exclude_lines):
                return False
            if aesthetic is not None:
                file = self.get_file_from_path(path=path)
                return file.aesthetic == aesthetic
            return True

        unpack_target = Path.get_cache_dir() / "Python"
        package_path = platform.download(path=unpack_target, overwrite=True)
        return self.path.get_differing_files(target=package_path, filt=filt)


    def compare_local_to_github(self, aesthetic=None):
        """ Get a list of changed files compared to remote with optional aesthetic files.

            :param generalpackager.Packager self:
            :param aesthetic: """
        return self._compare_local(platform=self.github, aesthetic=aesthetic)


    def compare_local_to_pypi(self, aesthetic=None):
        """ Get a list of changed files compared to pypi with optional aesthetic files.

            :param generalpackager.Packager self:
            :param aesthetic: """
        return self._compare_local(platform=self.pypi, aesthetic=aesthetic)

    def generate_setup(self):
        """ Generate setup.py.

            :param generalpackager.Packager self: """
        readme_path = self.localrepo.get_readme_path().relative(self.localrepo.get_setup_path().get_parent())
        last_version_split = self.python[-1].split(".")
        last_version_bumped_micro = f"{last_version_split[0]}.{int(last_version_split[1]) + 1}"
        setup_kwargs = {
            "name": f'"{self.localrepo.name}"',
            "author": f"'{self.author}'",
            "author_email": f'"{self.email}"',
            "version": f'"{self.localrepo.metadata.version}"',
            "description": f'"{self.localrepo.metadata.description}"',
            "long_description": "long_description",
            "long_description_content_type": '"text/markdown"',
            "install_requires": self.localrepo.metadata.install_requires,
            "url": f'"{self.github.url}"',
            "license": f'"{self.license}"',
            # "python_requires": f'">={self.python[0]}, <{last_version_bumped_micro}"',
            "packages": 'find_namespace_packages(exclude=("build*", "dist*"))',
            "extras_require": self.localrepo.metadata.extras_require,
            "classifiers": self.get_classifiers(),
            # "include_package_data": True,
        }

        top = CodeLine()
        top.add_node(CodeLine("from setuptools import setup, find_namespace_packages", space_before=1))
        top.add_node(CodeLine("from pathlib import Path", space_after=1))

        top.add_node(CodeLine("try:")).add_node(CodeLine("long_description = (Path(__file__).parent / 'README.md').read_text(encoding='utf-8')"))
        top.add_node(CodeLine("except FileNotFoundError:")).add_node(CodeLine("long_description = 'Readme missing'", space_after=1))

        setup = top.add_node(CodeLine("setup("))
        for key, value in setup_kwargs.items():
            if isinstance(value, list) and value:
                list_ = setup.add_node(CodeLine(f"{key}=["))
                for item in value:
                    list_.add_node(CodeLine(f"'{item}',"))
                setup.add_node(CodeLine("],"))
            elif isinstance(value, dict) and value:
                dict_ = setup.add_node(CodeLine(f"{key}={{"))
                for k, v in value.items():
                    dict_.add_node(CodeLine(f"'{k}': {v},"))
                setup.add_node(CodeLine("},"))
            else:
                setup.add_node(CodeLine(f"{key}={value},"))

        top.add_node(CodeLine(")"))

        return top.text()

    def generate_manifest(self):
        """ Generate manifest file.

            :param generalpackager.Packager self: """
        default_manifest = [
            self.localrepo.get_metadata_path().relative(self.path),
        ]
        return "\n".join([f"include {path}" for path in self.localrepo.metadata.manifest + default_manifest])

    def generate_git_exclude(self):
        """ Generate git exclude file.

            :param generalpackager.Packager self: """
        return "\n".join(self.git_exclude_lines)

    def generate_license(self):
        """ Generate LICENSE by using Packager.license.

            :param generalpackager.Packager self: """
        # text = Path(self.localrepo.get_repos_path() / f"generalpackager/generalpackager/licenses/{self.license}").text.read()
        text = (type(self)("generalpackager").path / "generalpackager/licenses" / self.license).text.read()

        assert "$" in text
        text = text.replace("$year", str(Date.now().datetime.year))
        text = text.replace("$author", self.author)
        assert "$" not in text

        return text

    def generate_workflow(self):
        """ Generate workflow.yml.

            :param generalpackager.Packager self: """
        workflow = CodeLine()
        workflow.indent_str = " " * 2

        workflow.add_node(self._get_name())
        workflow.add_node(self._get_triggers())
        workflow.add_node(self._get_defaults())

        jobs = workflow.add_node("jobs:")
        jobs.add_node(self._get_unittest_job())
        jobs.add_node(self._get_sync_job())

        return workflow.text()

    @staticmethod
    def set_collapsible(markdown):
        for child in markdown.get_children(include_self=True):
            if child.collapsible is None and child.header:
                child.collapsible = False

    def generate_init(self):
        """ Generate __init__.py.

            :param generalpackager.Packager self: """
        codeline = CodeLine(f"", space_before=1, space_after=50)

        return codeline

    def generate_randomtesting(self):
        """ Generate randomtesting.py.

            :param generalpackager.Packager self: """
        codeline = CodeLine(f"from {self.name} import *", space_before=1, space_after=50)

        return codeline

    def generate_generate(self):
        """ Generate randomtesting.py.

            :param generalpackager.Packager self: """
        top = CodeLine()
        top.add_node(CodeLine(f"from generalpackager import Packager", space_before=1, space_after=1))
        main = top.add_node(CodeLine(f'if __name__ == "__main__":'))
        main.add_node(CodeLine(f"""Packager("{self.name}").generate_localfiles(print_out=True)""", space_after=50))

        return top

    def generate_pre_commit(self):
        """ Generate test template.

            :param generalpackager.Packager self: """
        top = CodeLine()

        top.add_node(CodeLine("#!/usr/bin/env python"))
        top.add_node(CodeLine(f"from generalpackager import Packager", space_before=1))
        top.add_node(CodeLine(f"Packager(\"{self.name}\").generate_localfiles(aesthetic=False, error_on_change=True)", space_before=1))

        return top

    def generate_test_python(self):
        """ Generate test template.

            :param generalpackager.Packager self: """
        top = CodeLine()
        top.add_node(CodeLine("from unittest import TestCase", space_after=2))
        top.add_node("class Test(TestCase):").add_node("def test(self):").add_node("pass")

        return top

    def generate_npm_ignore(self):
        """ Generate .npmignore

            :param generalpackager.Packager self: """
        return "\n".join(self.npm_ignore_lines)

    def generate_index_js(self):
        """ Generate index.js

            :param generalpackager.Packager self: """
        top = CodeLine()
        top.add_node(CodeLine('exports.Vec2 = require("./vec2");', space_before=1, space_after=1))

        return top

    def generate_test_node(self):
        """ Generate test template.

            :param generalpackager.Packager self: """
        top = CodeLine()
        top.add_node("/**")
        top.add_node(" * @jest-environment jsdom")
        top.add_node(CodeLine(" */", space_after=1))
        top.add_node(CodeLine("// https://jestjs.io/docs/configuration#testenvironment-string", space_after=1))
        top.add_node(CodeLine('const Vec2 = require("./vec2");', space_after=1))
        top.add_node('test("Vec2 initializing", () => {').add_node("expect(new Vec2().x).toBe(0);")
        top.add_node("})")

        return top

    def generate_package_json(self):
        """ Generate test template.

            :param generalpackager.Packager self: """
        info = {
            "name": self.localrepo.name,
            "version": str(self.localrepo.metadata.version),
            "description": self.localrepo.metadata.description,
            "scripts": {
                "start": "parcel index.html",
                "build": "parcel build index.html",
                "test": "jest"
            },
            "dependencies": {dep: "latest" for dep in self.localrepo.dependencies},
            "devDependencies": {dep: "latest" for dep in self.localrepo.devDependencies},
            "keywords": self.get_topics(),
            "license": self.license,
            "author": self.author,
        }
        return json.dumps(info, indent=4)

    def generate_localfiles(self, aesthetic=True, print_out=False, error_on_change=False):
        """ Generate all local files.
            Returns True if any file is changed.

            :param aesthetic:
            :param generalpackager.Packager self:
            :param print_out:
            :param error_on_change: """
        timer = Timer()

        # Not in files because it writes with json not text, it's also a bit unique
        self.localrepo.metadata.name = self.name
        self.localrepo.metadata.write_config()

        files = [file for file in self.files if aesthetic or not file.aesthetic]

        for file in files:
            if print_out:
                print(f"Generating {file}")
            file.generate()
        if print_out:
            timer.print()

        if error_on_change:
            file_paths = {file.path for file in files}
            changed_files = {path.absolute() for path in self.localrepo.git_changed_files()}

            changed_generated_files = file_paths.intersection(changed_files)
            if changed_generated_files:
                raise EnvironmentError(f"Files changed: {changed_generated_files}")

























