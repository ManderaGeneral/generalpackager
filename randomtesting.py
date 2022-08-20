from dataclasses import dataclass, fields
from generalpackager import *
from generalfile import Path
from generallibrary import Recycle, SigInfo, getsize


with Path("generalpackager/api").as_working_dir():
    print(Packager("Mandera").path)


"""

    Do this after run passes
        

Why does workflow clone its own package?
Is that even using the latest (current) repo?


A better workflow would be:
    Clone all packages but itself into /home/runner/work/
    Install all packages in /home/runner/work/ (In correct order)


"""

