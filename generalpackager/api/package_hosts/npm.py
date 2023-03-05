from generalpackager.api.shared.name import _SharedAPI
from generalpackager.api.shared.owner import _SharedOwner
from generalpackager.api.shared.protocols import PackageHostProtocol


class NPM(_SharedAPI, _SharedOwner, PackageHostProtocol):
    DEFAULT_OWNER = "mandera"
    def download(self, path=None, version=None, overwrite=False):
        pass

    def url(self):
        pass

    def exists(self):
        pass

    def get_owners_packages(self):
        pass

    def get_version(self):
        pass

    def get_date(self):
        pass

