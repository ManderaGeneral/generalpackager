from logging import getLogger

from generalfile import Path
from generallibrary import deco_cache
from generalpackager.api.shared.target import Targets


class DynamicRelativePath:
    def __get__(self, instance, owner):
        if instance:
            return Path(instance._relative_path)
        else:
            assert not instance.requires_instance(), f"Only an instantialized Packager can access '{owner.__name__}'."
            return Path(owner._relative_path)


class File:
    """ Instantiated if its owner is. """
    targets = Targets

    _relative_path = ...
    aesthetic = ...  # Does this file affect unittests or not?

    remove = False
    overwrite = True
    is_file = True
    target = None

    def _generate(self):
        return ""

    def __init__(self, owner):
        """ :param generalpackager.Packager or generalpackager.LocalRepo owner: """
        self.owner = owner

    @property
    @deco_cache()
    def packager(self):
        return self.owner if type(self.owner).__name__ == "Packager" else None

    @property
    @deco_cache()
    def localrepo(self):
        return self.packager.localrepo if self.packager else self.owner

    relative_path = DynamicRelativePath()

    @classmethod
    def requires_instance(cls):
        return hasattr(cls._relative_path, "fget")

    @property
    @deco_cache()
    def path(self):
        return self.owner.path / self._relative_path

    @classmethod
    def has_generate_instructions(cls):
        return cls._generate is not File._generate

    def _cant_write(self, msg):
        logger = getLogger(__name__)
        logger.info(f"Can't write '{self.relative_path}' - {msg}")
        return False

    def can_write(self):
        if not self.is_file:
            return self._cant_write(".is_file is False")

        elif self.remove:
            return self._cant_write(".remove is True")

        elif not self.has_generate_instructions():
            return self._cant_write("._generate is undefined")

        elif self.target is not None and self.target != self.owner.target:
            return self._cant_write(f".target {self.target} doesn't match its owner's {self.owner}")

        elif self.overwrite is False and self.path.exists():
            return self._cant_write(f".overwrite is False and path {self.path} exists")

        else:
            return True

    def generate(self):
        logger = getLogger(__name__)
        if self.can_write():
            logger.info(f"Writing to '{self.relative_path}' for '{self.owner.name}'")
            return self.path.text.write(text=f"{self._generate()}\n", overwrite=self.overwrite)
        elif self.remove:
            logger.info(f"Deleting '{self.relative_path}' for '{self.owner.name}'")
            self.path.delete()

    def __str__(self):
        return f"<File: {self.owner.name} - {self.relative_path}>"
