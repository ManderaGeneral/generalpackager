from generallibrary import deco_cache

from generalpackager.api.shared.files.file_fetcher import FileFetcher
from generalfile import Path
from generalpackager.api.shared.files.helpers import _Files_Helpers


class _Files(_Files_Helpers):
    """ LocalRepo and Packager inherits this.
        Combines paths with generation instructions.
        Only an instance of Packager will return file instances. """
    file_definition_names = []

    @deco_cache()
    def get_files(self):
        """ :param generalpackager.Packager or generalpackager.LocalRepo self: """
        return [getattr(self, name) for name in self.file_definition_names]

    @deco_cache()
    def get_files_by_relative_path(self):
        """ :param generalpackager.Packager or generalpackager.LocalRepo self: """
        return {file.relative_path: file for file in self.get_files()}

    @deco_cache()
    def get_file_from_path(self, path):
        """ :param generalpackager.Packager or generalpackager.LocalRepo self: """
        path = Path(path).relative(self.path)
        return self.get_files_by_relative_path().get(path)

    # Generated with Packager._get_file_fetcher_definitions()
    commit_editmsg_file = FileFetcher()
    examples_folder = FileFetcher()
    exeproduct_folder = FileFetcher()
    exetarget_file = FileFetcher()
    generate_file = FileFetcher()
    git_exclude_file = FileFetcher()
    index_js_file = FileFetcher()
    init_file = FileFetcher()
    license_file = FileFetcher()
    manifest_file = FileFetcher()
    metadata_file = FileFetcher()
    npm_ignore_file = FileFetcher()
    org_readme_file = FileFetcher()
    package_json_file = FileFetcher()
    pre_commit_hook_file = FileFetcher()
    pre_push_hook_file = FileFetcher()
    readme_file = FileFetcher()
    setup_file = FileFetcher()
    test_folder = FileFetcher()
    test_js_file = FileFetcher()
    test_template_file = FileFetcher()
    workflow_file = FileFetcher()


