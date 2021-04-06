
from generalpackager import Packager
from generalfile import Path
from pprint import pprint
import sys
from generallibrary import Timer, Ver, print_link_to_obj, get_definition_line, ObjInfo, SigInfo

from generalpackager.api.github import GitHub
from generalpackager.api.local_repo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.pypi import PyPI


# HERE ** LocalRepo is getting wrong path

# print(Path.get_working_dir())

# packager = Packager()

with Path("generalpackager").as_working_dir():
    print(LocalRepo("generalfile"))
    # print(Path.get_working_dir().open_folder())

# packager.github.download(path=Path().absolute().get_parent() / "foo")


