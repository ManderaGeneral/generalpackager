
from generallibrary import remove_duplicates, deco_cache, Log, Timer, flatten

from itertools import chain

class _PackagerRelations:
    def get_dependencies(self, only_general=False):
        """ Get a list of dependencies as Packagers.
            Combines localmodules dependencies with localrepos install_requires.
            Optionally only return general packages.

            :param generalpackager.Packager self:
            :param bool only_general: Whether to only return general packages. """

        names = {localmodule.name for localmodule in self.localmodule.get_dependencies()}

        if self.target == self.Targets.python:
            names.update(self.localrepo.metadata.install_requires)

        return {type(self)(name) for name in names if not only_general or self.name_is_general(name)}

        # packagers = {type(self)(localmodule.name) for localmodule in self.localmodule.get_dependencies() if not only_general or self.name_is_general(localmodule.name)}
        # packagers.update({type(self)(name) for name in self.localrepo.metadata.install_requires if not only_general or self.name_is_general(name)})
        # return list(packagers)

    def get_dependants(self, only_general=False):
        """ Get a list of dependants as Packagers.
            Same as localmodules but Packager instead of localmodule.
            Optionally only return general packages.

            :param generalpackager.Packager self:
            :param bool only_general: Whether to only return general packages. """
        packagers = {type(self)(localmodule.name) for localmodule in self.localmodule.get_dependants() if not only_general or self.name_is_general(localmodule.name)}
        return list(packagers)

    def is_enabled(self):
        """ :param generalpackager.Packager self: """
        return self.is_general() and self.localrepo.metadata and self.localrepo.metadata.enabled

    def get_ordered_packagers(self, include_private=True, include_summary_packagers=False):
        """ Get a list of enabled ordered packagers from the dependency chain, sorted by name in each lvl.

            :param generalpackager.Packager or Any self:
            :param include_private:
            :param include_summary_packagers:
            :rtype: list[generalpackager.Packager] """
        # packagers = [packager for packager_set in packager.get_ordered(flat=False) for packager in sorted(packager_set, key=lambda x: x.name)]
        packagers_by_layer = self.get_ordered(flat=False, filt=type(self).is_enabled)
        sorted_layers = [sorted(layer, key=lambda pkg: pkg.name) for layer in packagers_by_layer]
        packagers = flatten(sorted_layers)

        if not include_private:
            packagers = [packager for packager in packagers if not packager.localrepo.metadata.private]

        if include_summary_packagers:
            packagers.extend(self.summary_packagers())

        Log().debug("Ordered packagers:", packagers)

        return packagers

    def get_owners_package_names(self):
        """ Return a set of owner's packages with intersecting PyPI and GitHub, ignores enabled flag.

            :param generalpackager.Packager self: """
        return self.pypi.get_owners_packages().intersection(self.github.get_owners_packages())

    def general_bumped_set(self):
        """ Return a set of general packagers that have been bumped.

            :param generalpackager.Packager self: """
        return {packager for packager in self.get_all() if packager.is_bumped()}

    def general_changed_dict(self, aesthetic=None):
        """ Return a dict of general packagers with changed files comparing to github.

            :param generalpackager.Packager self:
            :param aesthetic: """
        return {packager: files for packager in self.get_all() if (files := packager.compare_local_to_github(aesthetic=aesthetic))}

    @deco_cache()
    def get_untested_objInfo_dict(self):
        """ :param generalpackager.Packager self:
            :rtype: dict[generallibrary.ObjInfo] """
        if not self.localmodule.objInfo:
            return {}

        filt = lambda objInfo: not self.localrepo.text_in_tests(text=objInfo.name)
        all_objInfo = self.localmodule.objInfo.get_all(filt=filt, traverse_excluded=True)
        return {objInfo.name: objInfo for objInfo in all_objInfo}
