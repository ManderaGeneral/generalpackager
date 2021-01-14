
from generallibrary import TreeDiagram, ObjInfo
from generalpackager import Packager

import generallibrary
import generalpackager
from generalfile import Path

# HERE **

# Got it working finally! long_description relative is wrong. CI SYNC doesnt trigger actions


packager = Packager("generalpackager")
packager.generate_workflow()
# packager.generate_localfiles()
# packager.sync_package("Testing auto")

# packager.sync_github_metadata()
# packager.generate_git_exclude()
# packager.generate_setup()
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
# Todo: Write [CI MAJOR] in commit message to bump major for example
# Todo: Remove test/main.py
# Old workflow failed as we got duplicates in dependents for some reason, but I'm thinking we'll ignore that as we're moving to replace it.
