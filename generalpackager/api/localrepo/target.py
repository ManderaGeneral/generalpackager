
from generallibrary import classproperty, DataClass

from typing import Literal


class _LocalRepo_Target:
    """ Target of None is only for packages without a metadata.json file. """
    class Targets(DataClass):
        python = "python"
        npm = "npm"
        django = "django"
        exe = "exe"

    target = None

    def __init_subclass__(cls, **kwargs):
        assert cls.target in cls.Targets.keys()


    @classproperty
    def target_is_None(cls):    return cls.target is None
    @classproperty
    def target_is_python(cls):  return cls.target == "python"
    @classproperty
    def target_is_npm(cls):     return cls.target == "npm"
    @classproperty
    def target_is_django(cls):  return cls.target == "django"
    @classproperty
    def target_is_exe(cls):     return cls.target == "exe"


