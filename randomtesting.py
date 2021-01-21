
from generalpackager import Packager, PackagerGrp
from generalfile import Path

packager = Packager("generalpackager")
packager.file_workflow.generate()

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
# packager.localrepo.get_todos()
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
#
# PackagerGrp = PackagerGrp()
# print(PackagerGrp.packagers)
# print(PackagerGrp.get_bumped())


# Todo: Install packages in correct order when using git to prevent it using pip.

# Todo: Write [CI MAJOR] in commit message to bump major for example.
# Todo: Push empty commits to dependents after publish in workflow.
# Todo: Generate GitHub profile readme.
# Todo: Compare local_repo version with pypi version before publishing.

# Old workflow failed as we got duplicates in dependents for some reason, but I'm thinking we'll ignore that as we're moving to replace it.
