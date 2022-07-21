from typing import Literal

from generalfile import ConfigFile
from generallibrary import Ver


class Metadata(ConfigFile):
    enabled = True
    private = False
    name = None
    target: Literal["pypi", "github", "npm", "django", "exe"] = "pypi"
    version = Ver("0.0.1")
    description = "Missing description."
    install_requires = []
    extras_require = {}
    topics = []
    manifest = []

    # NPM, Used fpr npm and django target
    dependencies = []
    devDependencies = ["jest-environment-jsdom", "parcel"]

    def read_hook(self):
        extras_require = self.__dict__["extras_require"]
        if extras_require:
            keys = [key for key in extras_require.values() if key != "full"]
            extras_require["full"] = list(set().union(*keys))
            extras_require["full"].sort()
