
from generalpackager.api.shared import _SharedAPI
from generalpackager import PACKAGER_GITHUB_API
from generallibrary import Recycle, deco_cache

import requests
import json
import re



class GitHub(Recycle, _SharedAPI):
    """ Tools to interface a GitHub Repository. """
    _recycle_keys = {"name": str, "owner": str}

    def __init__(self, name=None, owner=None):
        if name is None:
            name = "generalpackager"
        if owner is None:
            owner = "ManderaGeneral"
        self.name = name
        self.owner = owner

        self.url = f"https://github.com/{self.owner}/{self.name}"

    def exists(self):
        """ Return whether this API's target exists. """
        return requests.get(url=self.url).status_code == 200

    def get_owners_packages(self):
        """ Get a set of a owner's packages' names on GitHub. """
        return set(re.findall(f'"/{self.owner}/(.+)/hovercard"', requests.get(f"https://github.com/{self.owner}?tab=repositories").text))

    def _api_url(self, endpoint=None):
        """ Get URL from owner, name and enpoint. """
        return "/".join(("https://api.github.com", "repos", self.owner, self.name) + ((endpoint, ) if endpoint else ()))

    def get_website(self):
        """ Get website specified in repository details.

            :rtype: list[str] """
        return self._request(method="get").json()["homepage"]

    def set_website(self, website):
        """ Set a website for the GitHub repository. """
        return self._request(method="patch", name=self.name, homepage=website)

    def get_topics(self):
        """ Get a list of topics in the GitHub repository.

            :rtype: list[str] """
        return self._request(method="get", endpoint="topics").json()["names"]

    def set_topics(self, *topics):
        """ Set topics for the GitHub repository.

            :param str topics: """
        return self._request(method="put", endpoint="topics", names=topics)

    def get_description(self):
        """ Get a string of description in the GitHub repository.

            :rtype: list[str] """
        return self._request(method="get").json()["description"]

    def set_description(self, description):
        """ Set a description for the GitHub repository. """
        return self._request(method="patch", name=self.name, description=description)

    @deco_cache()
    def _request(self, method="get", url=None, endpoint=None, **data):
        """ :rtype: requests.Response """
        method = getattr(requests, method.lower())

        kwargs = {
            "headers": {"Accept": "application/vnd.github.mercy-preview+json"},
            "auth": (self.owner, PACKAGER_GITHUB_API.value),
        }
        if data:
            kwargs["data"] = json.dumps(data)
        if url is None:
            url = self._api_url(endpoint=endpoint)
        return method(url=url, **kwargs)















