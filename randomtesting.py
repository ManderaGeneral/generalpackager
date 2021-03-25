
from generalpackager import Packager
from generalfile import Path
from pprint import pprint
import sys
from generallibrary import Timer, Ver, print_link_to_obj, get_definition_line, ObjInfo, SigInfo

from generalpackager.api.github import GitHub
from generalpackager.api.local_repo import LocalRepo
from generalpackager.api.local_module import LocalModule
from generalpackager.api.pypi import PyPI



# print(Path().absolute().get_parent().set_working_dir())



# print(Packager())


for path in Path("generalpackager").get_children(filt=lambda x: x.match("packager_"), traverse_excluded=True):
    Path(f"generalpackager/test/test_{path.name()}").text.write("""

from generalpackager import Packager
from generalfile.test.setup_workdir import setup_workdir

import unittest


class TestPackager(unittest.TestCase):
    pass
""", overwrite=True)

