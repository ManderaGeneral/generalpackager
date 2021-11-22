
from generalpackager import Packager
from generalfile import Path
from pprint import pprint
import sys
from generallibrary import Timer, Ver, print_link_to_obj, get_definition_line, ObjInfo, SigInfo, EnvVar, remove_duplicates, import_module

from generalpackager.api.github import GitHub
from generalpackager.api.local_repo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.pypi import PyPI


x = Packager()
# x.generate_localfiles()


for y in x.get_ordered_packagers():
    # y.file_workflow.generate()
    y.generate_localfiles(print_out=True)
    # print(y)

# x.file_randomtesting.generate()
# x.file_test_template.generate()



# Once that's fixed, look at mindmap, create generalmainframe (first private general repo)
# Move code from mainframe_api to generalbrowser and manderageneral
# Then continue with making purchasing products work



# x = Packager("generalgui")
# x.localrepo.generate_exe("randomtesting.py")

# HERE ** Try uploading exe to mainframe api


# print(x.compare_local_to_pypi(aesthetic=False))

# x.localrepo.pip_uninstall()
# x.path.delete()
# x.create_blank()



