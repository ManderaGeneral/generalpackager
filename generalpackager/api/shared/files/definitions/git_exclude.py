
from generalpackager.api.shared.files.file import File


class GitExcludeFile(File):
    _relative_path = ".git/info/exclude"
    is_file = False

    def generate(self):
        return "\n".join(self.packager.git_exclude_lines)

