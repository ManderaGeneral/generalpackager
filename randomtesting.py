import json
import os
from dataclasses import dataclass, fields
from importlib import import_module

import pkg_resources

from generalpackager import *
from generalfile import Path
from generallibrary import Recycle, SigInfo, getsize, Log, replace

from pprint import pprint


x = GitHub().get_topics()

print(x)

GitHub().set_topics(*x, "test")

x.remove("test")

GitHub().set_topics(*x)
