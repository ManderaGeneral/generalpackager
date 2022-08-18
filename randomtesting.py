from dataclasses import dataclass, fields
from generalpackager import *
from generalfile import Path
from generallibrary import Recycle, SigInfo

print(Packager().file_by_path("README.md").generate())
