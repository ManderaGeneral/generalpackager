
from generalpackager.api.shared.target import Targets, _SharedTarget


class _LocalRepo_Target(_SharedTarget):
    """ Target of None is only for packages without a metadata.json file. """
    _cls_metadata = None
    _cls_target_classes = {}

    def __init_subclass__(cls, **kwargs):
        """ :param generalpackager._LocalRepos_DOCS cls: """
        super().__init_subclass__(**kwargs)
        if cls.__name__ != cls._BASE_CLS_NAME:
            assert cls.target in Targets.field_values_defaults()
            assert cls._cls_metadata is not None
        cls._cls_target_classes[cls.target] = cls


