

class _Metadata:
    name = ...
    version = ...
    description = ...
    install_requires = ...
    extras_require = ...
    topics = ...

    def __init__(self, packager):
        self.packager = packager

        for key, value in self.packager.localrepo.get_metadata_path().read().items():
            setattr(self, key, value)

        for key in dir(self):
            if getattr(self, key) is Ellipsis:
                raise AssertionError(f"Key '{key}' for {self.packager}'s metadata is still ...")

    def _convert_topic(self, topic):
        if topic.startswith("python"):
            major = topic[6]
            minor = topic[7:]
            return f"Programming Language :: Python :: {major}.{minor}"
        return self._lib[topic]

    def _get_classifiers_from_topics(self):
        """ Get a list of classifiers generated from topics. """
        return [self._convert_topic(topic) for topic in self.topics]

    def get_classifiers(self):
        """ Get a complete list of classifiers generated from topics and other metadata. """
        # HERE ** Generate from license, python and os
        return self._get_classifiers_from_topics()

    _lib = {
        "planning": "Development Status :: 1 - Planning",
        "pre-alpha": "Development Status :: 2 - Pre-Alpha",
        "alpha": "Development Status :: 3 - Alpha",
        "beta": "Development Status :: 4 - Beta",
        "production/Stable": "Development Status :: 5 - Production/Stable",
        "mature": "Development Status :: 6 - Mature",
        "inactive": "Development Status :: 7 - Inactive",

        "utility": "Topic :: Utilities",

        "tool": "Topic :: Software Development :: Build Tools",
        "library": "Topic :: Software Development :: Libraries",
        "gui": "Topic :: Software Development :: User Interfaces",

        "file-manager": "Topic :: Desktop Environment :: File Managers",

        "mit-license": "License :: OSI Approved :: MIT License",

        "windows": "Operating System :: Microsoft :: Windows",
        "macos": "Operating System :: MacOS",
        "linux": "Operating System :: POSIX :: Linux",
    }

