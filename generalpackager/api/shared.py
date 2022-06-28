

class _SharedAPI:
    @staticmethod
    def name_is_general(name):
        return name.startswith("general") or name in ("manderageneral", )

    def is_general(self):
        """ Return whether name is general or not.

            :param generalpackager.api.pypi.PyPI or generalpackager.api.local_module.LocalModule or generalpackager.api.local_repo.LocalRepo or generalpackager.api.github.GitHub self: """
        return self.name_is_general(name=self.name)
