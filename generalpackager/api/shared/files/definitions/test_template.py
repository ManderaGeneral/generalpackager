
from generalpackager.api.shared.files.file import File


class TestTemplateFile(File):
    @property
    def _relative_path(self):
        return f"{self.packager.name}/test/test_{self.packager.name}.py"

    overwrite = False
    is_file = False

    def generate(self):
        pass

