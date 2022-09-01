from generalfile import Path
from generallibrary import Log

from generalpackager import Packager




Log("generalpackager").configure_stream()

with Path(".../general").as_working_dir():
    print(Packager.new_clean_environment())

#     lib = Packager("generallibrary", path="generallibrary", target="python")
#     mainframe = Packager("generalmainframe", path="generalmainframe", target="python")
#
#     print(mainframe.github.download())
#     print(lib.github.download())






