from generalfile import Path
from pprint import pprint
import sys
import json
from generallibrary import Timer, Ver, print_link_to_obj, get_definition_line, ObjInfo, SigInfo, EnvVar, remove_duplicates, import_module, Log, deco_extend

# from generalpackager import Packager
# from generalpackager.api.github import GitHub
from generalpackager.api.localrepo.local_repo import LocalRepo
# from generalpackager.api.local_module import LocalModule
# from generalpackager.api.pypi import PyPI



localrepo = LocalRepo("")

print(localrepo.metadata)  # HERE ** How would we initialize a new package with a sepcific target?



