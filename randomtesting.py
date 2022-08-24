from dataclasses import dataclass, fields
from importlib import import_module

import pkg_resources

from generalpackager import *
from generalfile import Path
from generallibrary import Recycle, SigInfo, getsize, Log



Packager().file_by_relative_path("setup.py").generate()


# Log().configure_stream()

# with Path("../generallibrary").as_working_dir():
#     print(LocalModule().get_dependencies())

# print([str(name) for name in pkg_resources.working_set.by_key["generalpackager"].requires()])

# Packager().file_by_relative_path(".github/workflows/workflow.yml").generate()  # HERE ** Create new workflow described below




"""
    Do this after run passes
        

Why does workflow clone its own package?
Is that even using the latest (current) repo?


A better workflow would be:
    Clone all packages but itself into /home/runner/work/
    Install all packages in /home/runner/work/ (In correct order)
"""

