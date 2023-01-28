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

        for packager in cls.packagers_from_packages():
            packager.github.download(path=repo_path)

        # HERE ** How do I install the packages in correct order?
        # Will they already be installed so that I can get_ordered_packagers?
        #   Well yeah they'll have to be otherwise I wouldn't be able to use this method







