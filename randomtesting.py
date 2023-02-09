import os
import re
import sys
from pprint import pprint

from generalfile import Path
from generallibrary import Log, Terminal, EnvVar
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv




# Log("root").configure_stream()

# print(Packager("generaltool", "../generaltool").localrepo.pip_install_editable())

# print(Packager.new_clean_environment(".../"))

# print(Packager.get_ordered_packagers())

# print(Venv.get_active_venv().debug())



# Venv.get_active_venv().cruds.Path_easy_install.set_value(value="hii")

print(Packager().localrepo.pip_install_editable())



















