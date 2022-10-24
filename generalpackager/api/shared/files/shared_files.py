from generalpackager.api.shared.files.file_fetcher import FileFetcher


class _Files:
    """ LocalRepo and Packager inherits this.
        Only an instance of Packager will return file instances. """
    randomtesting_file = FileFetcher()
    pre_push_hook_file = FileFetcher()
    exetarget_file = FileFetcher()
    org_readme_file = FileFetcher()
    readme_file = FileFetcher()
    test_file = FileFetcher()
    generate_file = FileFetcher()
    pre_commit_hook_file = FileFetcher()
    init_file = FileFetcher()
    setup_file = FileFetcher()
    test_template_file = FileFetcher()
    exeproduct_file = FileFetcher()
    metadata_file = FileFetcher()
    index_js_file = FileFetcher()
    test_js_file = FileFetcher()
    package_json_file = FileFetcher()
    license_file = FileFetcher()
    workflow_file = FileFetcher()
    git_exclude_file = FileFetcher()
    npm_ignore_file = FileFetcher()
    examples_file = FileFetcher()
    manifest_file = FileFetcher()


# if __name__ == "__main__":
#     from generalfile import Path
#     for definition in Path("./definitions").get_children():
#         file = definition.stem()
#         if file.startswith("_"):
#             continue
#         print(f"{file}_file = FileFetcher()")

