

class _PackagerRelations:
    packagers_dict = {}

    def __init__(self, name):
        if name in self.packagers_dict:
            raise AttributeError(f"{name} packager already exists")
        self.packagers_dict[name] = self

    def update_links(self):
        """ Update links of all created Packagers.

            :param generalpackager.Packager self: """
        for packager in self.packagers_dict.values():
            for dependency_name in packager.localrepo.install_requires:
                dependency_packager = self.packagers_dict.get(dependency_name)
                if dependency_packager is not None:
                    dependency_packager.link(target=packager)

    def get_packager_with_name(self, name):
        """ Return connected Packager or None.

            :param generalpackager.Packager self:
            :param name: """
        packager = self.packagers_dict.get(name)
        if packager is None and self.is_creatable(name=name):
            packager = type(self)(name=name, repos_path=self.repos_path)
        self.update_links()
        return packager

    def load_general_packagers(self):
        """ Load packagers with names.

            :param generalpackager.Packager self: """
        for name in self.get_users_package_names():
            self.get_packager_with_name(name=name)

    def get_dependencies(self):
        """ Get set of loaded Packagers that this Packager requires.

            :param generalpackager.Packager self: """
        return self.get_nodes(incoming=True, outgoing=False)

    def get_dependents(self):
        """ Get set of loaded Packagers that requires this Packager.

            :param generalpackager.Packager self: """
        return self.get_nodes(incoming=False, outgoing=True)

    def get_ordered_names(self):
        """ Get a list of ordered names from the dependency chain.

            :param generalpackager.Packager self: """
        return [packager.name for packager_set in self.get_ordered() for packager in sorted(packager_set, key=lambda x: x.name)]

    @classmethod
    def get_users_package_names(cls, pypi_user=None, github_user=None):
        """ Return a set of user's packages with intersecting PyPI and GitHub.

            :param generalpackager.Packager cls:
            :param pypi_user:
            :param github_user: """
        return cls.PyPI.get_users_packages(user=pypi_user).intersection(cls.GitHub.get_users_packages(user=github_user))



