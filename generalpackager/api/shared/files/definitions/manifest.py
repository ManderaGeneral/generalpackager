
from generalpackager.api.shared.files.file import File


class ManifestFile(File):
    _relative_path = "MANIFEST.in"
    aesthetic = False

    def generate(self):
        pass

