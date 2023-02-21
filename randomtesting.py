import os
import re
import sys
from pprint import pprint

from generalfile import Path
from generallibrary import Log, Terminal, EnvVar, AutoInitBases
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv




# print(list(Packager().localrepo.list_packages(editable=False)))
print(list(Packager("genlibrary").localrepo.list_packages(editable=False)))




