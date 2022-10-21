
from generalpackager.api.shared.files.file import File


class InitFile(File):
    _relative_path = "__init__.py"
    aesthetic = False
    overwrite = False

    def generate(self):
        pass

