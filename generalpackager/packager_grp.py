
from generalpackager import Packager
from generalpackager.api.local_repo import LocalRepo


class PackagerGrp:
    """ Handles a collection of packages. """
    def __init__(self, repos_path=None):
        self.repos_path = LocalRepo.get_repos_path(path=repos_path)

        self.packagers = []
        self.load_general_packages()

    def load_general_packages(self):
        """ Load my general packages. """
        self.add_packages(*Packager.get_users_packages())

    def add_packages(self, *names):
        """ Add a Package. """
        self.packagers.extend([Packager(name=name, repos_path=self.repos_path) for name in names])

    def clone(self):
        """ Clone all packages to repos_path. """
        for packager in self.packagers:
            packager.clone_repo()

    def install(self):
        """ Install all packages. """
        for packager in self.packagers:
            packager.localrepo.pip_install()

    def get_bumped(self):
        """ Get a list of bumped packagers, meaning PyPI version and LocalRepo version mismatch. """
        # return [(packager.localrepo.version, packager.pypi.get_version()) for packager in self.packagers if packager.is_bumped()]
        return [packager for packager in self.packagers if packager.is_bumped()]

    # def test(self):

