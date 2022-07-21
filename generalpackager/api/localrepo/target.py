
from generallibrary import classproperty, DataClass

from typing import Literal


class _LocalRepo_Target:
    """ Target of None is only for packages without a metadata.json file. """
    class Targets(DataClass):
        python = "python"
        npm = "npm"
        django = "django"
        exe = "exe"

    cls_target = None
    cls_target_classes = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        assert cls.__name__ == "LocalRepo" or cls.cls_target in cls.Targets.field_values_defaults()
        cls.cls_target_classes[cls.cls_target] = cls

    def extended(self):
        """ Return another LocalRepo object which has extended functionality based on target of metadata.

            :param generalpackager.LocalRepo self: """
        if self.metadata.exists():
            return self.cls_target_classes[self.metadata.target](path=self.path)


    @classmethod
    def target_is_None(cls):    return cls.cls_target is None
    @classmethod
    def target_is_python(cls):  return cls.cls_target == cls.Targets.python
    @classmethod
    def target_is_npm(cls):     return cls.cls_target == cls.Targets.npm
    @classmethod
    def target_is_django(cls):  return cls.cls_target == cls.Targets.django
    @classmethod
    def target_is_exe(cls):     return cls.cls_target == cls.Targets.exe


