import re

from generalfile import Path
from generallibrary import Log, Timer

from generalpackager import Packager

paths = (
"readme",
"org_readme",
"metadata",
"git_exclude",
"setup",
"manifest",
"license",
"workflow",
"test",
"test_template",
"init",
"randomtesting",
"generate",
"exetarget",
"exeproduct",
"git_ignore",
"npm_ignore",
"index_js",
"test_js",
"package_json",
"pre_commit_hook",
"pre_push_hook",
"examples",
)

base = Path("generalpackager/api/shared/files/definitions")

code = """
from generalpackager.api.shared.files.file import File


class ReadmeFile(File):
    _relative_path = "README.md"
    type = File.types.folder

    def generate(self):
        pass

"""


for name in paths:
    relative_path = f"{name}.py"
    path = base / relative_path
    class_name = "".join([part.capitalize() for part in name.split("_")]) + "File"

    path.text.write(code.replace("ReadmeFile", class_name).replace("README.md", relative_path), overwrite=True)




# from generalpackager import Packager
#
# packager = Packager()

# print(packager.get_attributes_markdown())

# print(packager.get_ordered_packagers(include_private=False))


# packager.get_parents(depth=1)
# print(packager.get_parents(depth=-1))
# print(packager.get_dependencies())
# print(packager.get_all())
# Path("hi.md").text.write(packager.get_mermaid_markdown(), overwrite=True)





# packager.file_by_relative_path(".git/hooks/pre-commit").generate()



# packager.file(packager.localrepo.get_pre_commit_hook_path()).generate()
# packager.get_pre_commit_hook_path().generate()



# Log("generalpackager").configure_stream()

# genlib = Packager("genlibrary")

# genlib.enable_vcs_operations()
# genlib.create_github_repo()
# genlib.create_master_branch()
# genlib.commit_and_push()


# with Path(".../general").as_working_dir():
#     print(Packager.new_clean_environment())
#
#     lib = Packager("generallibrary", path="generallibrary", target="python")
#     mainframe = Packager("generalmainframe", path="generalmainframe", target="python")
#
#     print(mainframe.github.download())
#     print(lib.github.download())






