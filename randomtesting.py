from dataclasses import dataclass, fields
from generalpackager import *
from generalfile import Path
from generallibrary import Recycle, SigInfo, getsize



print([packager.path for packager in Packager().get_all()])

# Path().absolute().view_paths(spawn=False)



"""

    Do this after run passes

Why does workflow clone its own package?
Is that even using the latest (current) repo?


A better workflow would be:
    Clone all packages but itself into /home/runner/work/
    Install all packages in /home/runner/work/ (In correct order)


"""

