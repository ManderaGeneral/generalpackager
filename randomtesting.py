
from generallibrary import TreeDiagram, ObjInfo
from generalpackager import Packager

import generallibrary
import generalpackager
from generalfile import Path


packager = Packager("generalpackager")
packager.generate_readme()
# packager.generate_workflow()
# packager.generate_localfiles()
# packager.sync_package("Clead up secrets, testing auto")
# packager.localrepo.get_todos()
# packager.sync_github_metadata()
# packager.generate_git_exclude()
# packager.generate_setup()
# packager.setup_all("Trying to make github token work.")

# packager.localrepo.get_git_exclude_path().open_folder()



# Todo: Write [CI MAJOR] in commit message to bump major for example

# Old workflow failed as we got duplicates in dependents for some reason, but I'm thinking we'll ignore that as we're moving to replace it.
