

class _PackagerRelations:
    def get_ordered_packagers(self):
        """ Get a list of ordered packagers from the dependency chain, sorted by name in each lvl.

            :param generalpackager.Packager self: """
        return [packager for packager_set in self.get_ordered(flat=False) for packager in sorted(packager_set, key=lambda x: x.name)]

    def get_owners_package_names(self):
        """ Return a set of owner's packages with intersecting PyPI and GitHub.

            :param generalpackager.Packager self: """
        return self.pypi.get_owners_packages().intersection(self.github.get_owners_packages())

    def general_bumped_set(self):
        """ Return a set of general packagers that have been bumped.

            :param generalpackager.Packager self: """
        return {packager for packager in self.get_all() if packager.is_bumped()}

    def general_changed_dict(self, aesthetic=False):
        """ Return a dict of general packagers with changed files comparing to remote.

            :param generalpackager.Packager self:
            :param aesthetic: """
        return {packager: files for packager in self.get_all() if (files := packager.compare_local_to_remote(aesthetic=aesthetic))}

