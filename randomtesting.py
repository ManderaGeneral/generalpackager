import os
import sys
from pprint import pprint

from generalfile import Path
from generallibrary import Log, Terminal, EnvVar
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv


venv_path = Path(r"C:\Python\Venvs\test2")

Venv.debug()
Venv(venv_path).activate()
Venv.debug()





































