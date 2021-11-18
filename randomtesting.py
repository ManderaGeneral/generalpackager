
from generalpackager import Packager
from generalfile import Path
from pprint import pprint
import sys
from generallibrary import Timer, Ver, print_link_to_obj, get_definition_line, ObjInfo, SigInfo, EnvVar, remove_duplicates

from generalpackager.api.github import GitHub
from generalpackager.api.local_repo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.pypi import PyPI




# x = Packager("generalmainframe")
x = Packager("generalpackager")
# print(x.get_ordered_packagers())
# x.create_blank()
# x.generate_localfiles()


x.commit_and_push("[CI SKIP] testing")  # HERE ** fix error below, workflows for other packages will automatically be updated when blank one is uploaded
# Automatic upload in create_blank? Should work
# Just realized generalmainframe should NOT be uploaded as it's private, that should be a setting to prevent upload

# self.commit_sha = remote.push()[0].summary.split("..")[1].rstrip()
# IndexError: list index out of range


# for packager in x.get_ordered_packagers():
#     packager.commit_and_push(["CI SKIP"])
    # packager.generate_localfiles()



# HERE ** generalbrowser wasn't uploaded with version 0.0.1 - Not sure why

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



