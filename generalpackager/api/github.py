
import requests
import os
import json


class GitHub:
    """ Tools to interface a GitHub Repository. """
    def __init__(self, owner, repo):
        self.owner = owner
        self.repo = repo

    def get_topics(self):
        """ Get a list of topics in the GitHub repository.

            :rtype: list[str] """
        return self._request(method="get", endpoint="topics").json()["names"]

    def set_topics(self, topics):
        """ Set a list of topics for the GitHub repository. """
        return self._request(method="put", endpoint="topics", names=topics)


    def get_description(self):
        """ Get a string of description in the GitHub repository.

            :rtype: list[str] """
        return self._request(method="get").json()["description"]

    def set_description(self, description):
        """ Set a description for the GitHub repository. """
        return self._request(method="patch", name=self.repo, description=description)



    def _token(self):
        return os.environ['packager_github_api']

    def _request(self, method, endpoint=None, **data):
        method = getattr(requests, method)

        url = f"https://api.github.com/repos/{self.owner}/{self.repo}"
        if endpoint:
            url += f"/{endpoint}"

        kwargs = {
            "headers": {"Accept": "application/vnd.github.mercy-preview+json"},
            "auth": (self.owner, self._token()),
        }
        if data:
            # kwargs["data"] = data
            kwargs["data"] = json.dumps(data)

        return method(url=url, **kwargs)
