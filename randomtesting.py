
from generalpackager import Packager
from generalfile import Path
from pprint import pprint
import sys
from generallibrary import Timer, Ver, print_link_to_obj, get_definition_line, ObjInfo, SigInfo, EnvVar

from generalpackager.api.github import GitHub
from generalpackager.api.local_repo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.pypi import PyPI


# print(Packager(name="Mandera", github_owner="Mandera").generate_personal_readme())

# Packager().file_workflow.generate()  # HERE ** CI is removing env vars

# print(Packager(name="Mandera", github_owner="Mandera"))


print(Packager().localmodule.get_env_vars())


