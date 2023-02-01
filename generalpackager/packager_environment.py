from generalfile import Path
from generallibrary import Log

from generalpackager.api.venv import Venv


class _PackagerEnvironment:
    @classmethod
    def new_clean_environment(cls, path=None, python_version=None):
        """ Creates a new clean environment for the packages.
            - Create, upgrade, and activate venv
            - Clone repos
            - Editable repo installs in venv

            :param generalpackager.Packager cls: """
        path = Path(path=path)
        path.open_folder()
        assert path.empty()
        if input("Proceed with creating a new clean environment in this folder? ").lower() != "y":  # This could be a general Path method
            return
        Log().configure_stream()

        repo_path = path / "repos"
        venv = Venv(path / "venvs")
        venv.create_venv(ver=python_version)
        venv.upgrade()

        for packager in cls.packagers_from_packages():  # This will get all packages
            packager.github.download(path=repo_path)

        for packager in cls.get_ordered_packagers():  # This will only get python packages
            packager.localrepo.pip_install_editable()






