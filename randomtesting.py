
from generallibrary import TreeDiagram, ObjInfo
import generallibrary
from generalpackager import *
from generalfile import Path


# packager = Packager("generalpackager")
# packager.sync_github_metadata()
# packager.generate_git_exclude()
# packager.generate_setup()
# packager.generate_workflow()
# packager.setup_all("Trying to make github token work.")

# packager.localrepo.get_git_exclude_path().open_folder()

# Todo: Automatically insert empty line when indent retracts

# Todo: Idea: Generate test.main file to run all unittests in folder, so that we can give arguments to unittests (Token)
#   Need to come up with a general solution for this.
#       How does a package specify which env vars it needs and with what GitHub actions var to fill them with?
#   python -m generalpackager.test.main <TOKEN>


# Old workflow failed as we got duplicates in dependents for some reason, but I'm thinking we'll ignore that as we're moving to replace it.


import sys
import os


def test():
    print(sys.argv)


test()
