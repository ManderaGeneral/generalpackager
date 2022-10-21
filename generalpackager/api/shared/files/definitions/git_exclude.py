
from generalpackager.api.shared.files.file import File


class GitExcludeFile(File):
    _relative_path = ".git/info/exclude"
    is_file = False


