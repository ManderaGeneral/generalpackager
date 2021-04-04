
from generalpackager import Packager
from generalfile import Path
from pprint import pprint
import sys
from generallibrary import Timer, Ver, print_link_to_obj, get_definition_line, ObjInfo, SigInfo

from generalpackager.api.github import GitHub
from generalpackager.api.local_repo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.pypi import PyPI


packager = Packager()

print(packager)

# print(packager.compare_local_to_pypi())
print(packager.compare_local_to_github())


# print(localrepo.get_changed_files())  # HERE ** Fix compare_local_to_pypi, compare_local_to_remote and get_changed_files
# Move to GitHub and change names to download

# for path in Path("generalpackager/test/tests/x").get_children(-1, filt=Path.is_file, traverse_excluded=True):
#     path.delete()


# Packager().commit_and_push("[CI SKIP] Auto tests.")
# Packager().file_workflow.generate()

# print(Packager("generalfile").localrepo.unittest())




# for packager in Packager().get_all():
    # print(packager)
    # packager.file_workflow.generate()


