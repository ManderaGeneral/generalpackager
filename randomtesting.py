
from generallibrary import TreeDiagram, ObjInfo
import generallibrary
from generalpackager import *
from generalfile import Path


packager = Packager("generalpackager")
# packager.generate_git_exclude()
# packager.generate_setup()
packager.generate_workflow()
# packager.setup_all("Trying to make github token work.")

# packager.localrepo.get_git_exclude_path().open_folder()

# Todo: Automatically insert empty line when indent retracts


# Old workflow failed as we got duplicates in dependents for some reason, but I'm thinking we'll ignore that as we're moving to replace it.

