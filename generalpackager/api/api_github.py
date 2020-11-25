
import requests
import os
import json

from generalpackager.api.api import _API


class APIGitHub(_API):
    """ All APIGitHub specific methods. """
    topics = ...
    _headers = {
        "Accept": "application/vnd.github.mercy-preview+json",
        # "Authorization": f"token {os.environ['packager_github_api']}",
    }
    _token = os.environ['packager_github_api']
    def __init__(self, owner, name):
        self.owner, self.name = owner, name
        self.load()

    def load(self):
        """ Load values from GitHub into self's attrs.
            Calls API attrs' correlating `get_*` methods. """
        for key in self.get_api_attrs():
            setattr(self, key, getattr(self, f"get_{key}")())

    def get_topics(self):
        """ Fetch topics as a list. """
        return requests.get(f"https://api.github.com/repos/{self.owner}/{self.name}/topics", headers=self._headers).json().get("names")

    def set_topics(self, topics):
        """ Send a request to change topics. """
        url = f"https://api.github.com/repos/{self.owner}/{self.name}/topics"
        data = json.dumps({"names": topics})
        return requests.put(url, auth=(self.owner, self._token), headers=self._headers, data=data)




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
