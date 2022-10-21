
from generalfile import Path
from generallibrary import deco_cache, classproperty

from generalpackager.api.localrepo.base.targets import Targets


class File:
    targets = Targets

    _relative_path = ...
    aesthetic = ...

    remove = False
    overwrite = True
    is_file = True
    target = Targets.python

    def generate(self):
        return ""

    def __init__(self, packager):
        """ :param generalpackager.Packager packager: """
        self.packager = packager

    @classmethod
    def requires_instance(cls):
        return hasattr(cls._relative_path, "fget")

    @classproperty
    @deco_cache()
    def relative_path(cls):
        return Path(cls._relative_path)

    @property
    @deco_cache()
    def path(self):
        return self.packager.path / self._relative_path

    def can_write(self):
        return self.generate is not File.generate and self.type != self.types.folder

    def write(self):
        if self.can_write():
            self.path.text.write(text=f"{self.generate()}\n", overwrite=self.overwrite)

    def __str__(self):
        return f"<File: {self.packager.name} - {self.relative_path}>"
