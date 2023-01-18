import sys

from generalfile import Path
from generallibrary import Log, Terminal
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv

# Log("root").configure_stream()
# Packager().localrepo.commit()
# Packager.new_clean_environment(Path(".../general"))


# print(Venv("C:\Python\Venvs\dev11").python_path())

# print(Terminal("-c", "assert 5 == 4", python=True, error=False, capture_output=False).string_result)


# print(Packager().get_ordered_packagers())

# print(Packager.summary_packagers()[0].org_readme_file.path)


Log("root").configure_stream()

print(Packager.summary_packagers()[0].org_readme_file.can_write())


