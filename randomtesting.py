import sys
from pprint import pprint

from generalfile import Path
from generallibrary import Log, Terminal
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv

# Log("root").configure_stream()
# Packager().localrepo.commit()


# print(Venv("C:\Python\Venvs\dev11").python_path())

# print(Terminal("-c", "assert 5 == 4", python=True, error=False, capture_output=False).string_result)



# print(Packager.summary_packagers()[0].org_readme_file.path)


# Log("root").configure_stream()

path = Path(".../general")

venv_path = Path(r"C:\Python\Venvs\test2")
# venv_path = Path(r"C:\Python\Venvs\dev11")

# path.open_folder()
# venv_path.open_folder()

# print(Packager().get_ordered_packagers())
# Packager.new_clean_environment(path)


venv = Venv(venv_path)

# print(venv.python_version())
# print(venv.virtualenv_version())
print(Path.get_active_venv())
# venv.create_venv()


# pprint(Venv("C:\Python\Venvs\dev11").python_version())



































