from generalpackager.api.shared.owner import _SharedOwner
from generalpackager.api.shared.name import _SharedName, _SharedAPI
from generalpackager.api.shared.protocols import PackageHostProtocol

from generallibrary import Ver, Date, get
from generalfile import Path

import requests
import re


class NPM(_SharedAPI, _SharedOwner, _SharedName, PackageHostProtocol):
    pass
