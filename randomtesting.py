from dataclasses import dataclass, fields
from importlib import import_module

import pkg_resources

from generalpackager import *
from generalfile import Path
from generallibrary import Recycle, SigInfo, getsize, Log


import yaml

from pprint import pprint

print(yaml.safe_load(Path(".github/workflows/workflow.yml").text.read()))

# Packager().file_by_relative_path(".github/workflows/workflow.yml").generate()

