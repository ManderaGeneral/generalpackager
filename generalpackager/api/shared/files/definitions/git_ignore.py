
from generalpackager.api.shared.files.file import File


class GitIgnoreFile(File):
    _relative_path = ".gitignore"
    is_file = False


