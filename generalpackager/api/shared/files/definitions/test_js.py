
from generalpackager.api.shared.files.file import File


class TestJsFile(File):
    _relative_path = "test.js"
    aesthetic = False
    overwrite = False
    target = File.targets.node

    def generate(self):
        pass

