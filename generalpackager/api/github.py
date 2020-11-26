
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
        return self._request_get("topics")["names"]

    def set_topics(self, topics):
        """ Set a list of topics for the GitHub repository. """
        return self._request_set("topics", names=topics)


    def get_description(self):
        """ Get a string of description in the GitHub repository.

            :rtype: list[str] """
        return self._request_get("")

    def set_description(self, description):
        """ Set a description for the GitHub repository. """
        return self._request_set("", name=self.repo, description=description)



    def _token(self):
        return os.environ['packager_github_api']

    def _request(self, endpoint, get_or_put, **kwargs):
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}"
        if endpoint:
            url += f"/{endpoint}"

        headers={"Accept": "application/vnd.github.mercy-preview+json"}
        return get_or_put(url=url, headers=headers, **kwargs).text

    def _request_get(self, endpoint):
        return self._request(endpoint=endpoint, get_or_put=requests.get)

    def _request_set(self, endpoint, **data):
        print(json.dumps(data))
        return self._request(endpoint=endpoint, get_or_put=requests.patch, auth=(self.owner, self._token()), data=json.dumps(data))



