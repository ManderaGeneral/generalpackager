from generalfile import Path
from generallibrary import deco_cache

from generalpackager.api.shared.files.base import File


class ReadmeFile(File):
    _relative_path = "README.md"
    aesthetic = True

    def generate(self):
        pass




