
from generallibrary import DataClass
from generalpackager.api.localrepo.base.metadata import Metadata


class _LocalRepo_Target:
    """ Target of None is only for packages without a metadata.json file. """

    _BASE_CLS_NAME = "LocalRepo"

    cls_target = None
    cls_metadata = Metadata

    cls_target_classes = {}

    class Targets(DataClass):
        python = "python"
        node = "node"
        django = "django"
        exe = "exe"

    assert set(Metadata.field_dict_literals()["target"]) == set(Targets.field_values_defaults()), "Targets aren't synced, couldn't make this DRY."

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        assert cls.__name__ == cls._BASE_CLS_NAME or cls.cls_target in cls.Targets.field_values_defaults()
        assert cls.__name__ == cls._BASE_CLS_NAME or cls.cls_metadata is not Metadata

        cls.cls_target_classes[cls.cls_target] = cls

    def targetted(self, target=...):
        """ Return another LocalRepo object which has extended functionality based on target of metadata.

            :param generalpackager.LocalRepo self:
            :param target:
            :rtype: generalpackager.api.localrepo.node.localrepo_node.LocalRepo_Node or generalpackager.api.localrepo.python.localrepo_python.LocalRepo_Python """

        if target is Ellipsis and self.metadata.exists():
            target = self.metadata.target

        if target is None:
            return self
        else:
            return self.cls_target_classes[target](path=self.path)


