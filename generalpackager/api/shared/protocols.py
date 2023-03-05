""" Not using typing.Protocol because that's for type checking only.
    Not using abc because I don't want to define an extra metaclass.
        The only thing that'd be nice is if it'd detect unchanged stubs. """
from typing import List


class PackageHostProtocol:
    """ GitHub.com, PyPI.org, NPMjs.com"""
    DEFAULT_OWNER = ...
    def __init__(self, name=None, owner=None): pass
    def download(self, path=None, version=None, overwrite=False): raise NotImplementedError
    def url(self): raise NotImplementedError
    def exists(self): raise NotImplementedError
    def get_owners_packages(self): raise NotImplementedError
    def get_version(self): raise NotImplementedError
    def get_date(self): raise NotImplementedError


class LocalRepoProtocol:
    """ Python and Node target. """
    def install(self, local=True, editable=False): raise NotImplementedError
    def uninstall(self, local=True, editable=False): raise NotImplementedError
    def run_tests(self): raise NotImplementedError
    def publish(self, public=True): raise NotImplementedError

    def list_packages(self, local=True, editable=None) -> List[str]: raise NotImplementedError

