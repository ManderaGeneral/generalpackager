
from generallibrary import TreeDiagram, ObjInfo
import generallibrary
from generalpackager import *
from generalfile import Path


packager = Packager("generalpackager")
packager.generate_setup()
# packager.generate_workflow()
# packager.setup_all("Added automatic version bumping.")

# HERE ** Next up is workflow generation

# packager.generate_workflow()

# Todo: Automatically insert empty line when indent retracts

