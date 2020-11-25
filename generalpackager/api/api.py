
from generallibrary import attributes, remove_duplicates
from itertools import chain


class _API:
    def get_api_attrs(self):
        """ Get a dict of class variables defined by this api, default value is `None`. """
        return attributes(self, methods=False, properties=False, from_instance=False, from_bases=False)

    name, version, description, install_requires, extras_require, classifiers, topics = ..., ..., ..., ..., ..., ...

    def set_api_attrs(self, attrs):
        """ Load a dict into self's attributes.

            :param generalpackager.APIs self:
            :param attrs: """
        for key, value in attrs.items():
            setattr(self, key, value)



        if self.extras_require is not ...:
            self.extras_require["full"] = remove_duplicates([package for package in chain(*list(self.extras_require.values()))])

        if self.topics is not ...:
            self.topics += "python37", "python38", "windows7", "windows10", "linux", "macos", "unittest"



_topic_to_classifier = {
    "library": "Topic :: Software Development :: Libraries",
    "tools": "Topic :: Software Development :: Build Tools",

    "planning": "Development Status :: 1 - Planning",
    "pre-alpha": "Development Status :: 2 - Pre-Alpha",
    "alpha": "Development Status :: 3 - Alpha",
    "beta": "Development Status :: 4 - Beta",
    "stable": "Development Status :: 5 - Production/Stable",
    "mature": "Development Status :: 6 - Mature",
    "inactive": "Development Status :: 7 - Inactive",

    "python37": "Programming Language :: Python :: 3.7",
    "python38": "Programming Language :: Python :: 3.8",
    "python39": "Programming Language :: Python :: 3.9",

    "windows7": "Operating System :: Microsoft :: Windows :: Windows 7",
    "windows10": "Operating System :: Microsoft :: Windows :: Windows 10",
    "linux": "Operating System :: POSIX :: Linux",
    "macos": "Operating System :: MacOS",

    "unittest": "Topic :: Software Development :: Testing :: Unit",
}

