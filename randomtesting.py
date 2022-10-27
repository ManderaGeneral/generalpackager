
from generalfile import Path
from generallibrary import Log
from generalpackager import Packager, LocalRepo



# Packager().commit_and_push("Cleaned up PackagerGitHub, #18 done")
# Packager().push()

packager = Packager()

packager.localrepo.add_all()
packager.localrepo.commit("testing sha")
print(packager.localrepo.repo.head.object.hexsha)

packager.push()

print(packager.commit_sha)

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






