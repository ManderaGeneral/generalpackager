class FileClsOrInst:
    """ Descriptor to return instance of a File if instance owner is Packager.
        Otherwise, return class of File.
        Caches File instance to instance of Packager. """
    def __init__(self, cls):
        """ :param generalpackager.api.shared.files.file.File or Any cls: """
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
            assert self.cls.requires_instance(), f"Can only access {self.cls} through an instance of Packager."
            return self.cls
