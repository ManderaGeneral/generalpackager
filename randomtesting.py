import json
import os
from dataclasses import dataclass, fields
from importlib import import_module

import pkg_resources

from generalpackager import *
from generalfile import Path
from generallibrary import Recycle, SigInfo, getsize, Log, replace

from pprint import pprint


print(Packager("generallibrary").localrepo.unittest())


