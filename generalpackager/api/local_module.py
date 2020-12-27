
from generallibrary import ObjInfo, Markdown


class LocalModule:
    """ Tools to interface a Local Python Module. """
    def __init__(self, module):
        self.module = module

        self.objInfo = ObjInfo(self.module)
        self.objInfo.filters = [self._filter]

        assert self.objInfo.is_module()
        self._generate_attributes()

    def _filter(self, objInfo):
        """ :param ObjInfo objInfo: """
        return objInfo.public() and not objInfo.is_module()

    def _generate_attributes(self):
        self.objInfo.get_attrs(depth=-1)


    def _custom_repr(self, objInfo):
        return objInfo.name

    @staticmethod
    def _doc(objInfo):
        return objInfo.doc(only_first_line=True, require_sentence=True)

    def get_attributes_markdown(self):
        """ Get attributes markdown.
            One table for each class and one for all functions. """
        # self.objInfo.view()

        attributes = Markdown(header="Public attributes")
        namespace = Markdown(header="Namespace", parent=attributes)

        namespace_objInfos = self.objInfo.get_children()
        namespace_dicts = []

        for objInfo in namespace_objInfos:  # type: ObjInfo
            objInfo_children = objInfo.get_children()
            added_class_namespace = objInfo.is_class() and objInfo_children
            if added_class_namespace:
                class_dicts = []
                for objInfo_child in objInfo_children:  # type: ObjInfo
                    class_dicts.append({
                        "Method": objInfo_child.name,
                        "Doc": self._doc(objInfo_child),
                    })
                Markdown(header=f"Class: {objInfo.name}", parent=namespace).add_table_lines(*class_dicts)

            namespace_dicts.append({
                "Name": Markdown.link(text=objInfo.name, url=f"Class: {objInfo.name}", enabled=added_class_namespace),
                "Doc": self._doc(objInfo),
            })

        namespace.add_table_lines(*namespace_dicts)
        namespace.lines.append("<hr>")

        return attributes





























