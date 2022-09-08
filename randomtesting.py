from generalfile import Path
from generallibrary import Log

from generalpackager import Packager


# stacktester = Packager.create_blank_locally_python("../other/stacktester", install=False)
# print(stacktester)


Packager().get_examples_markdown()

# packager = Packager()

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






