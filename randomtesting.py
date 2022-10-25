
from generalfile import Path
from generallibrary import Log
from generalpackager import Packager, LocalRepo


print(Packager().commit_editmsg_file)
print(LocalRepo().commit_editmsg_file)  # HERE ** This should be able to resolve with LocalRepo's path, when fixed go to next bookmark



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






