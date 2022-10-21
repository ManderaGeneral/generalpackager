
from generalpackager.api.shared.files.file import File


class IndexJsFile(File):
    _relative_path = "index.js"
    overwrite = False
    target = File.targets.node

    def generate(self):
        pass

