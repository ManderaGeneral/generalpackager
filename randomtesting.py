
from generallibrary import TreeDiagram, ObjInfo
from generalpackager import Packager

import generallibrary
import generalpackager
from generalfile import Path


packager = Packager("generalpackager")

print(packager.generate_test_main())

# packager.sync_github_metadata()
# packager.generate_git_exclude()
# packager.generate_setup()
# packager.generate_workflow()
# packager.setup_all("Trying to make github token work.")

# packager.localrepo.get_git_exclude_path().open_folder()


# Class EnvVar in lib
# Import EnvVar to packager to create an instance of github_token
# Import github_token throughout package and use like normal
# Packager's LocalModule will find all EnvVar instances with actions_name defined
# The name and actions_name for each instance is then used to create the command line to launch test.main.py







# import sys
# import os
# def test():
#     args = {split[0]: split[1] for arg in sys.argv[1:] if (split := arg.split("="))}
# test()


# Todo: Automatically insert empty line when indent retracts
# Old workflow failed as we got duplicates in dependents for some reason, but I'm thinking we'll ignore that as we're moving to replace it.
