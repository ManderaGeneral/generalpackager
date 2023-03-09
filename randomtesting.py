
import os
import re
import subprocess
import sys
from pprint import pprint

from generalfile import Path
from generallibrary import Log, Terminal, EnvVar, AutoInitBases, DecoContext
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv



genvector = Packager("genvector")

Log("root").configure_stream()

# print(genvector.localrepo._node_modules_path())

# genvector.localrepo.install(local=True)
# genvector.localrepo.uninstall(local=True)

print(list(genvector.localrepo.list_packages(local=True)))
print(list(genvector.localrepo.list_packages(local=False)))

# print(genvector.localrepo.package_folder(local=False))
# print(genvector.localrepo.package_folder(local=True))






