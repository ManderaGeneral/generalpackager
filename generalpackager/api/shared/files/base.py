from abc import ABC, abstractmethod
from generalfile import Path
from generallibrary import deco_cache, classproperty

from generalpackager.api.shared.files.definitions.readme import ReadmeFile


class FileClsOrInst:
    """ Descriptor to return instance of a File if instance owner is Packager.
        Otherwise, return class of File.
        Caches File instance to instance of Packager. """
    def __init__(self, cls):
        self.cls = cls

    @property
    def protected_name(self):
        return f"_{self.cls.__name__}"

    def __get__(self, instance, owner):
        if instance and type(instance).__name__ == "Packager":
            cached_file = getattr(instance, self.protected_name, None)
            if cached_file:
                return cached_file
            else:
                new_file = self.cls(packager=instance)
                setattr(instance, self.protected_name, new_file)
                return new_file
        else:
            return self.cls


class _Files:
    """ LocalRepo and Packager inherits this.
        Only an instance of Packager will return file instances. """
    readme = FileClsOrInst(cls=ReadmeFile)


class File(ABC):
    """ Time with and without abc. ** HERE """
    @property
    @abstractmethod
    def _relative_path(self):
        pass

    @property
    @abstractmethod
    def aesthetic(self):
        pass

    @abstractmethod
    def generate(self):
        pass

    def __init__(self, packager):
        """ :param generalpackager.Packager packager: """
        self.packager = packager

    @classproperty
    @deco_cache()
    def relative_path(cls):
        return Path(cls._relative_path)

    @property
    @deco_cache()
    def path(self):
        return self.packager.path / self._relative_path

    def overwrite(self):
        self.path.text.write(text=f"{self.generate()}\n", overwrite=True)

    def __str__(self):
        return f"<File: {self.packager.name} - {self.relative_path}>"
