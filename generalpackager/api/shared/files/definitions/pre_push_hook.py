
from generalpackager.api.shared.files.file import File


class PrePushHookFile(File):
    _relative_path = ".git/hooks/pre-push"
    aesthetic = True

    def generate(self):
        pass

