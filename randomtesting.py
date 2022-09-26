import re

from generalfile import Path
from generallibrary import Log, Timer

from generalpackager import Packager

import pstats
import cProfile

packager = Packager()

# pr = cProfile.Profile()
# pr.enable()
# pr.runcall(packager.get_parents, depth=1)
# pr.disable()
#
# p = pstats.Stats(pr)
# p.print_callers('_traverse')

with Timer():
    # packager.get_parents(depth=1)
    # print(packager.get_parents(depth=-1))
    # print(packager.get_dependencies())
    print(packager.get_all())


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






