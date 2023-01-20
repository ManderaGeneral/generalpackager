from generalfile import Path
from generallibrary import Log


class _PackagerEnvironment:
    @classmethod
    def new_clean_environment(cls, path=None, python_version=None):
        """ Creates a new clean environment for the packages.
            - Create, upgrade, and activate venv
            - Clone repos
            - Editable repo installs in venv

            :param generalpackager.Packager cls: """
        path = Path(path)
        assert path.empty()

        repo_path = path / "repos"
        venv_path = path / "venvs"

        if python_version is None:
            python_version = cls.python[-1]

        packagers = cls.packagers_from_packages()

        for packager in packagers:
            Log().info(f"Downloading {packager.name} from GitHub.")
            packager.github.download(path=repo_path)








