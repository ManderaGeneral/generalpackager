from generallibrary import CodeLine

from generalpackager.api.shared.files.file import File


class InitFile(File):
    _relative_path = "__init__.py"
    aesthetic = False
    overwrite = False

    def _generate(self):
        codeline = CodeLine(f"", space_before=1, space_after=50)
        return codeline

