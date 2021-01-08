
from generalpackager.api.local_repo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.github import GitHub
from generalpackager.api.pypi import PyPI
from generalpackager.packager import Packager



import os


class _EnvVar:
    """ actions_name has to be defined if the env var is used for unittesting in the workflow. """
    def __init__(self, name, actions_name=None):
        if name not in os.environ:
            raise KeyError(f"Env var '{name}' is not set.")

        if actions_name is not None:
            actions_name = "${{" + actions_name + "}}"

        self.name = name
        self.actions_name = actions_name
        self.value = os.environ[self.name]

github_token = _EnvVar("packager_github_api", "secrets.ACTIONS_TOKEN")
