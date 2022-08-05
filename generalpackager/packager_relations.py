
from generallibrary import remove_duplicates, deco_cache

from itertools import chain

class _PackagerRelations:
    def get_dependencies(self, only_general=False):
        """ Get a list of dependencies as Packagers.
            Combines localmodules dependencies with localrepos install_requires.

            :param generalpackager.Packager self:
            :param bool only_general: Whether to only return general packages. """
        # names = chain()

        packagers = {type(self)(localmodule.name) for localmodule in self.localmodule.get_dependencies() if not only_general or self.name_is_general(localmodule.name)}
        packagers.update({type(self)(name) for name in self.localrepo.metadata.install_requires if not only_general or self.name_is_general(name)})
        return list(packagers)

    def get_dependants(self, only_general=False):
        """ Get a list of dependants as Packagers.
            Same as localmodules but Packager instead of localmodule.

            :param generalpackager.Packager self:
            :param bool only_general: Whether to only return general packages. """
        packagers = {type(self)(localmodule.name) for localmodule in self.localmodule.get_dependants() if not only_general or self.name_is_general(localmodule.name)}
        return list(packagers)

    def get_ordered_packagers(self):
        """ Get a list of enabled ordered packagers from the dependency chain, sorted by name in each lvl.

            :param generalpackager.Packager self:
            :rtype: list[generalpackager.Packager] """
        return remove_duplicates([packager for packager_set in self.get_ordered(flat=False) for packager in sorted(packager_set, key=lambda x: x.name)])

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
