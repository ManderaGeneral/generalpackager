from dataclasses import dataclass, fields
from importlib import import_module

from generalpackager import *
from generalfile import Path
from generallibrary import Recycle, SigInfo, getsize, Log

# with Path("generalpackager/api").as_working_dir():
#     print(Packager("Mandera").path)


# Log().configure_stream()

# print(LocalModule(name="Mandera").module)


print(import_module(".api", "generalpackager").__file__)


# print(Packager.get_ordered_packagers())

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

