
from generalpackager import Packager
from generalfile import Path
from pprint import pprint
import sys
from generallibrary import Timer, Ver, print_link_to_obj, get_definition_line


# packager = Packager(name="Mandera", owner="Mandera")
# packager.file_personal_readme.generate()

# packager.commit_push_store_sha("Testing new personal readme generation.")


# packager = Packager("generalfile")
# print(packager.github_link_path_line("test", "generalpackager/packager_files.py"))


# print(packager.localmodule.objInfo.get_child_by_key_values(name="Path").get_child_by_key_values(name="size").get_definition_line())

# packager = Packager("generalfile")
packager = Packager("generalpackager")
packager.load_general_packagers()
# print(packager.generate_personal_readme())
packager.file_readme.generate()
# print(packager.generate_manifest())


# pprint(packager.get_todos())
# pprint(packager.get_todos())


# pprint(packager.compare_local_to_pypi(aesthetic=False))
# packager.file_manifest.generate()
# packager.file_setup.generate()
# packager.localrepo.commit_and_push("[CI SKIP] Getting tags to work", tag=True)


# packager.file_workflow.generate()

# packager.localrepo.pip_install()

# packager.generate_localfiles(aesthetic=False)

# print(packager.get_ordered_packagers())

# print(packager.localrepo.version)
# packager.localrepo.bump_version()
# print(packager.localrepo.version)

# print(packager.get_changed_files(aesthetic=False))
# print(packager.get_changed_files(aesthetic=True))
# print(packager.pypi.get_version())


# packager.localmodule.get_dependants("generallibrary")
# packager.generate_readme()
# packager.generate_localfiles()
# packager.sync_package("Cleaned up secrets, testing auto")
# packager.sync_github_metadata()
# packager.generate_git_exclude()
# packager.generate_setup()

# packager.localrepo.get_git_exclude_path().open_folder()

# print(GitHub.is_creatable("generalpackager", "ManderaGeneral"))
# print(LocalModule.is_creatable("generalpackager"))
# print(LocalRepo.is_creatable(packager.path))
# print(PyPI.is_creatable("generalpackager"))




# path = Path.get_working_dir().get_parent(1) / "testrepos"
# path.open_folder()

# packagerGrp = PackagerGrp()
# print(packagerGrp.get_dependency_order())

# print(packagerGrp.packagers)
# print(packagerGrp.get_bumped())



# Old workflow failed as we got duplicates in dependents for some reason, but I'm thinking we'll ignore that as we're moving to replace it.
