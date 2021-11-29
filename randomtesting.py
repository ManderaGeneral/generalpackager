
from generalpackager import Packager
from generalfile import Path
from pprint import pprint
import sys
from generallibrary import Timer, Ver, print_link_to_obj, get_definition_line, ObjInfo, SigInfo, EnvVar, remove_duplicates, import_module

from generalpackager.api.github import GitHub
from generalpackager.api.local_repo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.pypi import PyPI


# x = Packager("generalgui")
# x = Packager("generalpackager")
# x.generate_localfiles()
# x.localrepo.write_metadata()



# for y in x.get_ordered_packagers():  # manderageneral not included
#     print(y)
#     y.localrepo.write_metadata()
#     # y.file_workflow.generate()
#     # y.generate_localfiles(print_out=True)

# x.file_randomtesting.generate()
# x.file_test_template.generate()



# Once that's fixed, look at mindmap, create generalmainframe (first private general repo)
# Move code from mainframe_api to generalbrowser and manderageneral
# Then continue with making purchasing products work


print(list({"a": 1}))


# x = Packager("generalmainframe")
# x.localrepo.generate_exe("exetarget.py")

# HERE ** Try uploading exe to mainframe api


# print(x.compare_local_to_pypi(aesthetic=False))

# x.localrepo.pip_uninstall()
# x.path.delete()
# x.create_blank()



