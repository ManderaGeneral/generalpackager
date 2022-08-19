from dataclasses import dataclass, fields
from generalpackager import *
from generalfile import Path
from generallibrary import Recycle, SigInfo, getsize



print([packager.path for packager in Packager().get_all()])

# Path().absolute().view_paths(spawn=False)



