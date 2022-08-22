from dataclasses import dataclass, fields
from importlib import import_module

import pkg_resources

from generalpackager import *
from generalfile import Path
from generallibrary import Recycle, SigInfo, getsize, Log



# Log().configure_stream()

with Path("../generallibrary").as_working_dir():
    print(LocalModule().get_dependencies())

print([str(name) for name in pkg_resources.working_set.by_key["generalpackager"].requires()])




"""
So two issues
    Resolved path is allowed to not have correct stem
        Path is None, maybe module shouldnt exist if Path is None?
    Somehow Mandera is installed
        Name has (namespace) suffix
        It's not installed with pip_install
"""


"""
    Do this after run passes
        

Why does workflow clone its own package?
Is that even using the latest (current) repo?


A better workflow would be:
    Clone all packages but itself into /home/runner/work/
    Install all packages in /home/runner/work/ (In correct order)
"""

