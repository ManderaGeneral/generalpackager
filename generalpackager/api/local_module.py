
from generallibrary import ObjInfo, deco_cache, Recycle

import pkg_resources
from importlib import import_module


class LocalModule(Recycle):
    """ Tools to interface a Local Python Module. """
    _recycle_keys = {"name": str}

    def __init__(self, name=None):
        if name is None:
            name = "generalpackager"
        self.name = name

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

    @property
    @deco_cache()
    def objInfo(self):
        objInfo = ObjInfo(self.module)
        assert objInfo.is_module()
        objInfo.get_children(depth=-1, filt=self._filter, traverse_excluded=False)
        objInfo.disconnect(lambda node: not self._filter(node))
        return objInfo

    def _filter(self, objInfo):
        """ :param ObjInfo objInfo: """
        # print(objInfo.name, objInfo.module().__name__.startswith(self.name))
        return objInfo.module().__name__.startswith(self.name)

    def get_env_vars(self):
        """ Get a list of EnvVar instances avialable directly in module.

            :rtype: list[generallibrary.EnvVar] """
        filt = lambda objInfo: type(objInfo.obj).__name__ == "EnvVar"
        return [objInfo.obj for objInfo in self.objInfo.get_children(filt=filt)]

    @staticmethod
    def get_all_local_modules():
        """ Get a list of all available LocalModules. """
        return [LocalModule(name=pkg.project_name) for pkg in pkg_resources.working_set]

    def get_dependencies(self):
        """ Get a list of LocalModules that this module depends on. """
        return [LocalModule(name=str(name)) for name in pkg_resources.working_set.by_key[self.name.lower()].requires()]

    def get_dependants(self):
        """ Get a list of LocalModules that depend on this module. """
        return [local_module for local_module in self.get_all_local_modules() if self in local_module.get_dependencies()]


























