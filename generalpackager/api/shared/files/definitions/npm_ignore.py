
from generalpackager.api.shared.files.file import File


class NpmIgnoreFile(File):
    _relative_path = ".npmignore"
    aesthetic = True

    def generate(self):
        pass

