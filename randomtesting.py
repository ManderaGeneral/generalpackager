
from generalfile import Path
from generallibrary import Log, Terminal
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv

# Log("root").configure_stream()
# Packager().localrepo.commit()
# Packager.new_clean_environment(Path(".../general"))


# print(Venv("C:\Python\Venvs\dev11").python_path())

# print(Terminal("-c", "print(5)", python=True, error=False, capture_output=False).success())


print(Packager().get_ordered_packagers())




