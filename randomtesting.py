
from generalpackager import Packager
from generalfile import Path
from pprint import pprint
import sys
from generallibrary import Timer, Ver, print_link_to_obj, get_definition_line, ObjInfo, SigInfo, EnvVar, remove_duplicates

from generalpackager.api.github import GitHub
from generalpackager.api.local_repo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.pypi import PyPI


print(Packager(name="Mandera", github_owner="Mandera").generate_personal_readme())

# Packager().file_workflow.generate()  # HERE ** CI is removing env vars

# print(Packager(name="Mandera", github_owner="Mandera"))



# pprint(Packager().get_untested_objInfo_dict())
# print(Packager().get_attributes_markdown())

# pprint(Packager().get_todos(), width=500)





