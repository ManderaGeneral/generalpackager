from generalpackager.api.shared.files.cls_or_inst import FileClsOrInst

from generalpackager.api.shared.files.definitions.readme import ReadmeFile
from generalpackager.api.shared.files.definitions.generate import GenerateFile
from generalpackager.api.shared.files.definitions.test_js import TestJsFile
from generalpackager.api.shared.files.definitions.test import TestFile
from generalpackager.api.shared.files.definitions.pre_commit_hook import PreCommitHookFile
from generalpackager.api.shared.files.definitions.metadata import MetadataFile
from generalpackager.api.shared.files.definitions.examples import ExamplesFile
from generalpackager.api.shared.files.definitions.pre_push_hook import PrePushHookFile
from generalpackager.api.shared.files.definitions.package_json import PackageJsonFile
from generalpackager.api.shared.files.definitions.npm_ignore import NpmIgnoreFile
from generalpackager.api.shared.files.definitions.manifest import ManifestFile
from generalpackager.api.shared.files.definitions.init import InitFile
from generalpackager.api.shared.files.definitions.exetarget import ExetargetFile
from generalpackager.api.shared.files.definitions.org_readme import OrgReadmeFile
from generalpackager.api.shared.files.definitions.randomtesting import RandomtestingFile
from generalpackager.api.shared.files.definitions.exeproduct import ExeproductFile
from generalpackager.api.shared.files.definitions.workflow import WorkflowFile
from generalpackager.api.shared.files.definitions.index_js import IndexJsFile
from generalpackager.api.shared.files.definitions.setup import SetupFile
from generalpackager.api.shared.files.definitions.test_template import TestTemplateFile
from generalpackager.api.shared.files.definitions.git_exclude import GitExcludeFile
from generalpackager.api.shared.files.definitions.license import LicenseFile


class _Files:
    """ LocalRepo and Packager inherits this.
        Only an instance of Packager will return file instances. """
    randomtesting_file = FileClsOrInst(cls=RandomtestingFile)
    pre_push_hook_file = FileClsOrInst(cls=PrePushHookFile)
    exetarget_file = FileClsOrInst(cls=ExetargetFile)
    org_readme_file = FileClsOrInst(cls=OrgReadmeFile)
    readme_file = FileClsOrInst(cls=ReadmeFile)
    test_file = FileClsOrInst(cls=TestFile)
    generate_file = FileClsOrInst(cls=GenerateFile)
    pre_commit_hook_file = FileClsOrInst(cls=PreCommitHookFile)
    init_file = FileClsOrInst(cls=InitFile)
    setup_file = FileClsOrInst(cls=SetupFile)
    test_template_file = FileClsOrInst(cls=TestTemplateFile)
    exeproduct_file = FileClsOrInst(cls=ExeproductFile)
    metadata_file = FileClsOrInst(cls=MetadataFile)
    index_js_file = FileClsOrInst(cls=IndexJsFile)
    test_js_file = FileClsOrInst(cls=TestJsFile)
    package_json_file = FileClsOrInst(cls=PackageJsonFile)
    license_file = FileClsOrInst(cls=LicenseFile)
    workflow_file = FileClsOrInst(cls=WorkflowFile)
    git_exclude_file = FileClsOrInst(cls=GitExcludeFile)
    npm_ignore_file = FileClsOrInst(cls=NpmIgnoreFile)
    examples_file = FileClsOrInst(cls=ExamplesFile)
    manifest_file = FileClsOrInst(cls=ManifestFile)


if __name__ == "__main__":
    from generalfile import Path
    for definition in Path("./definitions").get_children():
        file = definition.stem()
        if file.startswith("_"):
            continue

        cls = "".join(part.capitalize() for part in file.split("_")) + "File"
        print(f"from generalpackager.api.shared.files.definitions.{file} import {cls}")
        print(f"{file}_file = FileClsOrInst(cls={cls})")

