import os
import re
import subprocess
import sys
from pprint import pprint

from generalfile import Path
from generallibrary import Log, Terminal, EnvVar, AutoInitBases
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv




# genlibrary = Packager("genlibrary")

# genlibrary.localrepo.install()

# pprint(dict(os.environ))

# print(Terminal("-c", "import os, pprint; pprint.pprint(dict(os.environ))", python=True).string_result)
# print(Terminal(r"C:\Users\ricka\AppData\Roaming\npm\npm.cmd", "--version").string_result)

# print(Terminal("npm.cmd", "--version").string_result)


# print(list(Packager("genlibrary").localrepo.list_packages(editable=False)))
# print(list(Packager("genlibrary").localrepo.list_packages(editable=False)))




