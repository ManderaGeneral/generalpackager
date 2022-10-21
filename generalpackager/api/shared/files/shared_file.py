from generalpackager.api.shared.files.cls_or_inst import FileClsOrInst
from generalpackager.api.shared.files.definitions.readme import ReadmeFile


class _Files:
    """ LocalRepo and Packager inherits this.
        Only an instance of Packager will return file instances. """
    readme_file = FileClsOrInst(cls=ReadmeFile)
