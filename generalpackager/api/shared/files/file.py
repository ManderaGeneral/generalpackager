
from generalfile import Path
from generallibrary import deco_cache

from generalpackager.api.localrepo.base.targets import Targets


class DynamicRelativePath:
    def __get__(self, instance, owner):
        if instance:
            return Path(instance._relative_path)
        else:
            return Path(owner._relative_path)  # No need to check for requires_instance() again


class File:
    """ Instantiated if its Packager is. """
    targets = Targets

    _relative_path = ...
    aesthetic = ...

    remove = False
    overwrite = True
    is_file = True
    target = Targets.python

    def _generate(self):
        return ""

    def __init__(self, packager):
        """ :param generalpackager.Packager packager: """
        self.packager = packager

    relative_path = DynamicRelativePath()

    @classmethod
    def requires_instance(cls):
        return hasattr(cls._relative_path, "fget")

    @property
    @deco_cache()
    def path(self):
        return self.packager.path / self._relative_path

    def can_write(self):
        return self._generate is not File._generate and self.is_file

    def generate(self):
        if self.can_write():
            return self.path.text.write(text=f"{self._generate()}\n", overwrite=self.overwrite)

    def __str__(self):
        return f"<File: {self.packager.name} - {self.relative_path}>"
