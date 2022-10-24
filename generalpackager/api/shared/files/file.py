
from generalfile import Path
from generallibrary import deco_cache

from generalpackager.api.localrepo.base.targets import Targets


class DynamicRelativePath:
    def __get__(self, instance, owner):
        if instance:
            return Path(instance._relative_path)
        else:
            assert not instance.requires_instance(), f"Only an instantialized Packager can access '{owner.__name__}'."
            return Path(owner._relative_path)


class File:
    """ Instantiated if its Packager is. """
    targets = Targets

    _relative_path = ...
    aesthetic = ...

    remove = False
    overwrite = True
    is_file = True
    target = Targets.python  # Should probably default to None, and then I put python on most files

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
        return type(self)._generate is not File._generate and self.is_file and self.target == self.packager.target

    def generate(self):
        if self.can_write():
            if self.overwrite is False and self.path.exists():
                return False
            return self.path.text.write(text=f"{self._generate()}\n", overwrite=True)

    def __str__(self):
        return f"<File: {self.packager.name} - {self.relative_path}>"
