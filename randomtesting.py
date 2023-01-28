import os
import sys
from pprint import pprint

from generalfile import Path
from generallibrary import Log, Terminal, EnvVar
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv

# - Upgrade pip
# - List installed Python versions if possible (Might end up just using python alias)

venv_path = Path(r"C:\Python\Venvs\test4")
venv = Venv(venv_path)

venv.activate()
# print(venv.upgrade())


































