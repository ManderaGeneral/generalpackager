
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

    def _get_table_dict(self, objInfo, link):
        """ :param ObjInfo objInfo: """
        return {
            "Name": Markdown.link(text=objInfo.name, header=objInfo.nice_repr(), enabled=link),
            "Type": objInfo.type(nice_output=True),
            "Description": objInfo.doc(only_first_line=True, require_sentence=True),
        }

    def get_attributes_markdown(self, packager):
        """ Get attributes markdown.
            One table for each class and one for all functions.
            Todo: Remove Namespaces if we get code links working. """
        # self.objInfo.view()

        attributes = Markdown(header="Public attributes")
        namespace = Markdown(header="Direct namespace", parent=attributes)
        attr_navigation = Markdown(header="Recursive attributes navigation", parent=attributes)
        namespace_attributes = Markdown(header="Namespace attributes", parent=attributes)


        namespace_objInfos = self.objInfo.get_children()
        namespace_dicts = {}
        class_dicts = {}

        for objInfo in namespace_objInfos:  # type: ObjInfo
            objInfo_children = objInfo.get_children()

            _added_class_namespace = objInfo.is_class() and objInfo_children
            namespace_dicts[objInfo.name] = self._get_table_dict(objInfo=objInfo, link=_added_class_namespace)

            if _added_class_namespace:
                class_dicts[objInfo.name] = [self._get_table_dict(objInfo=child, link=False) for child in objInfo_children]
                Markdown(header=objInfo.nice_repr(), parent=namespace_attributes).add_table_lines(*class_dicts[objInfo.name])

        namespace.add_table_lines(*namespace_dicts.values())


        def _nav_repr(objInfo_):
            """ :param ObjInfo objInfo_: """
            header_link = Markdown.link(objInfo_.nice_repr(), href=True, enabled=objInfo_.name in class_dicts.keys())

            owner = packager.github.owner
            repo_name = packager.name
            file_path = objInfo_.module_path(repo_name=repo_name)
            line = objInfo_.get_definition_line()
            commit_sha = packager.commit_sha
            code_link = Markdown.link_github_code(owner=owner, repo_name=repo_name, file_path=file_path, line=line, commit_sha=commit_sha)

            return f"{header_link} {code_link}"

        view_str = self.objInfo.view(custom_repr=_nav_repr, print_out=False)
        attr_navigation.add_pre_lines(view_str)

        return attributes



























