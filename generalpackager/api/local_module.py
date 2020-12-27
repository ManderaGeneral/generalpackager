
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

        namespace_objInfos = []
        classes = []

        for objInfo in self.objInfo.get_children():  # type: ObjInfo
            namespace_objInfos.append(objInfo)

            if objInfo.is_class() and objInfo.get_children():
                classes.append(objInfo)


        list_of_dicts = [{
                "Name": f"[{objInfo.name}](#class:-{objInfo.name})",
                "Doc": self._doc(objInfo)
            } for objInfo in namespace_objInfos]
        namespace = Markdown(header="Namespace", parent=attributes)
        namespace.add_table_lines(list_of_dicts=list_of_dicts)
        namespace.lines.append("<hr>")

        for objInfo_class in classes:
            list_of_dicts = [{
                    "Method": objInfo.name,
                    "Doc": self._doc(objInfo)
                } for objInfo in objInfo_class.get_children()]
            Markdown(header=f"Class: {objInfo_class.name}", parent=namespace).add_table_lines(list_of_dicts=list_of_dicts)

        # Markdown(markdown.view(print_out=False, custom_repr=self._custom_repr), header="Navigation", parent=markdown)#.set_index(0)
        # markdown.view()
        return attributes


