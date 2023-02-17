import os
import re
import sys
from pprint import pprint

from generalfile import Path
from generallibrary import Log, Terminal, EnvVar, AutoInitBases
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv



# Venv.get_active_venv().cruds.Path_easy_install.set_value(value="hii")
# Venv.get_active_venv().easy_install_path().open_folder()
# print(Packager().localrepo.pip_install_editable())


# print(Venv.get_active_venv().python_path(local=False))

# I want to list global packages for npm and python
# It's a mess now. Venv is only for local python.
# Make a new api?
# Make all go through LocalRepo? This seems reasonable, install and uninstall is already there

# import pip


# print(Packager("genlibrary"))
# print(list(Packager().localrepo.list_packages(editable=False)))





from pip._internal.cli.main import main

print(main(["list"]))




