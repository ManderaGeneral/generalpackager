import os
import re
import sys
from pprint import pprint

from generalfile import Path
from generallibrary import Log, Terminal, EnvVar
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv





# Venv.get_active_venv().cruds.Path_easy_install.set_value(value="hii")
# Venv.get_active_venv().easy_install_path().open_folder()
print(Packager().localrepo.pip_install_editable())



















