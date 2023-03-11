from generalpackager.api.localrepo.base.metadata import _Metadata
from generalpackager.api.shared.target import Targets


class Metadata_Node(_Metadata):
    target = Targets.node
    dependencies = []
    devDependencies = ["jest-environment-jsdom", "parcel"]
