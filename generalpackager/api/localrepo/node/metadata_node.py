from generalpackager.api.localrepo.base.metadata import Metadata

class Metadata_Node(Metadata):
    target = "node"
    dependencies = []
    devDependencies = ["jest-environment-jsdom", "parcel"]
