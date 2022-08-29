
from generalpackager.other.envvars import PACKAGER_GITHUB_API, TWINE_USERNAME, TWINE_PASSWORD

from generalpackager.packager import Packager

from generalpackager.api.localrepo.base.localrepo import LocalRepo
from generalpackager.api.localrepo.python.localrepo_python import LocalRepo_Python
from generalpackager.api.localrepo.node.localrepo_node import LocalRepo_Node

from generalpackager.api.localmodule import LocalModule
from generalpackager.api.github import GitHub
from generalpackager.api.pypi import PyPI


def interconnect(*objs):
    """ Todo: Put interconnect in lib and test. """
    for obj in objs:
        for obj2 in objs:
            if obj is obj2:
                continue
            setattr(obj, obj2.__name__, obj2)

interconnect(Packager, LocalRepo, LocalModule, GitHub, PyPI)
