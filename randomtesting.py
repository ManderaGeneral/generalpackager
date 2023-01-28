import os
import sys
from pprint import pprint

from generalfile import Path
from generallibrary import Log, Terminal, EnvVar
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv


venv_path = Path(r"C:\Python\Venvs\test4")
venv_path.delete_folder_content()
venv = Venv(venv_path)

venv.create_venv(python_path=r"C:\Users\ricka\AppData\Local\Programs\Python\Python39\python.exe")

print(venv.python_version())
# pprint(venv.list_python_versions())


# {'*': <Path: 'C:\Python\Venvs\dev11\Scripts\python.exe'>,
#  '3.10': <Path: 'C:\Users\ricka\AppData\Local\Programs\Python\Python310\python.exe'>,
#  '3.11': <Path: 'C:\Users\ricka\AppData\Local\Programs\Python\Python311\python.exe'>,
#  '3.9': <Path: 'C:\Users\ricka\AppData\Local\Programs\Python\Python39\python.exe'>}


























