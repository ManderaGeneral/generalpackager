
from generalpackager.api.shared.files.file import File


class LicenseFile(File):
    _relative_path = "LICENSE"
    aesthetic = True

    def generate(self):
        pass

