
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

    @staticmethod
    def _attr_repr(objInfo, packager):
        """ :param ObjInfo objInfo: """
        text = objInfo.nice_repr()
        owner = packager.github.owner
        repo_name = packager.name
        file_path = objInfo.module_path(repo_name=repo_name)
        line = objInfo.get_definition_line()
        commit_sha = packager.commit_sha

        return Markdown.link_github_code(text=text, owner=owner, repo_name=repo_name, file_path=file_path, line=line, commit_sha=commit_sha)

    def get_attributes_markdown(self, packager):
        """ Get attributes markdown.
            One table for each class and one for all functions.
            Todo: Remove Namespaces if we get code links working. """

        view_str = self.objInfo.view(custom_repr=lambda objInfo, packager=packager: self._attr_repr(objInfo, packager), print_out=False)
        return Markdown(header="Attributes").add_pre_lines(view_str)



























