
from generalpackager.api.shared.files.file import File


class ReadmeFile(File):
    _relative_path = "README.md"
    aesthetic = True

    def generate(self):
        pass
