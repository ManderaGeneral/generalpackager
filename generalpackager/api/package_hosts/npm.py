from generalpackager.api.shared.name import _SharedAPI
from generalpackager.api.shared.owner import _SharedOwner
from generalpackager.api.shared.protocols import PackageHostProtocol


class NPM(_SharedAPI, _SharedOwner, PackageHostProtocol):
    pass
