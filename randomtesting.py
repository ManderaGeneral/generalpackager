
from generalpackager import Packager
from generalfile import Path
from pprint import pprint
import sys
from generallibrary import Timer, Ver, print_link_to_obj, get_definition_line, ObjInfo, SigInfo, EnvVar, remove_duplicates

from generalpackager.api.github import GitHub
from generalpackager.api.local_repo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.pypi import PyPI


# packages = Packager().get_ordered_packagers()
# for p in packages:
#     p.localrepo.pip_install()
# print(packages)

# packager = Packager("generalpackager")
# packager.localrepo.pip_install()


# generalbrowser = Packager("generalbrowser")
# generalbrowser.localrepo.upload()



# HERE ** generalbrowser wasn't uploaded with version 0.0.1 - Not sure why
# Sync is also failing: https://github.com/ManderaGeneral/generalpackager/runs/4168506133?check_suite_focus=true

# Once that's fixed, look at mindmap, create generalmainframe (first private general repo)
# Move code from mainframe_api to generalbrowser and generalmainframe
# Then continue with making purchasing products work



# x = Packager("generalgui")
# x.localrepo.generate_exe("randomtesting.py")

# HERE ** Try uploading exe to mainframe api


# print(x.compare_local_to_pypi(aesthetic=False))

# x.localrepo.pip_uninstall()
# x.path.delete()
# x.create_blank()



