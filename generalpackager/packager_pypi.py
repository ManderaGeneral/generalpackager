
import subprocess


class _PackagerPypi:
    def create_sdist(self):
        """ Create source distribution.

            :param generalpackager.Packager self: """
        subprocess.call("python setup.py sdist bdist_wheel")

    def upload(self):
        """ Upload local repo to PyPI.

            :param generalpackager.Packager self: """
        self.create_sdist()
        subprocess.call("twine --version")
