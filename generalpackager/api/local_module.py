
from generalpackager.api.shared import _SharedAPI
from generallibrary import ObjInfo, deco_cache, Recycle, EnvVar

import pkg_resources
from importlib import import_module


class LocalModule(Recycle, _SharedAPI):
    """ Tools to interface a Local Python Module. """
    _recycle_keys = {"name": lambda name: LocalModule._scrub_name(name=name)}

    def __init__(self, name=None):
        self.name = self._scrub_name(name=name)

    @classmethod
    def _scrub_name(cls, name):
        return name or "generalpackager"

    def __repr__(self):
        return self.name

    def exists(self):
        """ Return whether this API's target exists. """
        try:
            import_module(name=self.name)
        except ModuleNotFoundError:
            return False
        return True

    @property
    @deco_cache()
    def module(self):
        return import_module(self.name)

    def _filter(self, objInfo):
        """ :param ObjInfo objInfo: """
        return objInfo.module().__name__.startswith(self.name) and (objInfo.from_class() or objInfo.from_module())

    @property
    @deco_cache()
    def objInfo(self):
        objInfo = ObjInfo(self.module)
        assert objInfo.is_module()
        objInfo.children_states[ObjInfo.is_instance] = False
        objInfo.get_children(depth=-1, filt=self._filter, traverse_excluded=False)
        objInfo.disconnect(lambda node: not self._filter(node))
        return objInfo

    # @deco_cache()
    def get_env_vars(self):
        """ Get a list of EnvVar instances available directly in module.

            :rtype: list[generallibrary.EnvVar] """
        new_objInfo = ObjInfo(self.module)

        new_objInfo.all_identifiers = []  # Bad fix for bad circularity prevention
        new_objInfo.spawned_children = False
        return [objInfo.obj for objInfo in new_objInfo.get_children() if isinstance(objInfo.obj, EnvVar)]

    @staticmethod
    @deco_cache()
    def get_all_local_modules():
        """ Get a list of all available LocalModules. """
        return [LocalModule(name=pkg.project_name) for pkg in pkg_resources.working_set]

    @deco_cache()
    def get_dependencies(self):
        """ Get a list of LocalModules that this module depends on. """
        return [LocalModule(name=str(name)) for name in pkg_resources.working_set.by_key[self.name.lower()].requires()]

    @deco_cache()
    def get_dependants(self):
        """ Get a list of LocalModules that depend on this module. """
        return [local_module for local_module in self.get_all_local_modules() if self in local_module.get_dependencies()]


























