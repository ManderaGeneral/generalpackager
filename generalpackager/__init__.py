
from generallibrary import EnvVar

github_token = EnvVar("packager_github_api", "secrets.ACTIONS_TOKEN")


from generalpackager.api.local_repo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.github import GitHub
from generalpackager.api.pypi import PyPI
from generalpackager.packager import Packager

