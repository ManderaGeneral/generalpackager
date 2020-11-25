
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
        self.set_api_attrs({key: getattr(self, f"get_{key}") for key in self.get_api_attrs()})

    def get_topics(self):
        """ Fetch topics as a list. """
        return requests.get(f"https://api.github.com/repos/{self.owner}/{self.name}/topics", headers=self._headers).json().get("names")

    def set_topics(self, topics):
        """ Send a request to change topics. """
        url = f"https://api.github.com/repos/{self.owner}/{self.name}/topics"
        data = json.dumps({"names": topics})
        return requests.put(url, auth=(self.owner, self._token), headers=self._headers, data=data)


