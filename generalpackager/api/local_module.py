
from generallibrary import ObjInfo, deco_cache

import pkg_resources
from importlib import import_module


class LocalModule:
    """ Tools to interface a Local Python Module. """
    def __init__(self, name):
        self.name = name

    @classmethod
    def exists(cls, name):
        """ Return whether this API can be created. """
        try:
            import_module(name=name)
        except ModuleNotFoundError:
            return False
        return True

    @deco_cache()
    @property
    def module(self):
        return import_module(self.name)

    @deco_cache()
    @property
    def objInfo(self):
        objInfo = ObjInfo(self.module)
        assert objInfo.is_module()
        objInfo.filters = [self._filter]
        objInfo.get_attrs(depth=-1)
        return objInfo

    def _filter(self, objInfo):
        """ :param ObjInfo objInfo: """
        is_part_of_module = objInfo.module().__name__.startswith(self.name)
        parent = objInfo.get_parent()
        return objInfo.public() and not (objInfo.is_instance() or objInfo.is_module()) and is_part_of_module and objInfo.name not in ("fget", "fset") and not objInfo.from_builtin() and (parent is None or parent.is_module() or parent.is_class())

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


























