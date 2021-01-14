
from generallibrary import EnvVar

# Todo: Rename secrets and cleanup.

github_token = EnvVar("packager_github_api", "secrets.PACKAGER_GITHUB_API")
GIT_PASSWORD = EnvVar("GIT_PASSWORD", "secrets.GIT_PASSWORD")


from generalpackager.api.local_repo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.github import GitHub
from generalpackager.api.pypi import PyPI
from generalpackager.packager import Packager

