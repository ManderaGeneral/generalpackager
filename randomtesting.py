
from generalfile import Path
from generallibrary import Log
from generalpackager import Packager, LocalRepo

import git
import github

# packager = Packager()
# print(type(packager.localrepo.repo))


# repo = packager.localrepo.repo
# head = repo.head
# commit = head.commit
#
# print(commit)
#
# repo.commit()
#
# print(packager.localrepo.repo.head.commit)


# print(packager.remote)


LocalRepo(path="hi").init_repo()


# localrepo = LocalRepo(path="hi")
# localrepo.init_repo()
# print(localrepo.commit_sha_short)

# packager = Packager()

# packager.localrepo.commit()


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






