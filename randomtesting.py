import re

from generalfile import Path
from generallibrary import Log, Timer

from generalpackager import Packager

# print(Packager().readme_file.aesthetic)
# print(Packager("generalfile").readme_file.aesthetic)


class Z:
    def __init__(self):
        print("init")

    def __set_name__(self, owner, name):
        print(owner, name)

class X:
    y = Z()






# Log("generalpackager").configure_stream()

# genlib = Packager("genlibrary")

# genlib.enable_vcs_operations()
# genlib.create_github_repo()
# genlib.create_master_branch()
# genlib.commit_and_push()


# with Path(".../general").as_working_dir():
#     print(Packager.new_clean_environment())
#
#     lib = Packager("generallibrary", path="generallibrary", target="python")
#     mainframe = Packager("generalmainframe", path="generalmainframe", target="python")
#
#     print(mainframe.github.download())
#     print(lib.github.download())






