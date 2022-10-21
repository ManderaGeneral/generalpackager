
from generalpackager.api.shared.files.file import File


class PackageJsonFile(File):
    _relative_path = "package.json"
    aesthetic = False
    target = File.targets.node

    def generate(self):
        pass

