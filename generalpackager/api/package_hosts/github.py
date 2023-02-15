import json

import requests

from generalfile import Path
from generallibrary import Log, Terminal
from generalpackager import GH_TOKEN
from generalpackager.api.shared.name import _SharedAPI
from generalpackager.api.shared.owner import _SharedOwner
from generalpackager.api.shared.protocols import PackageHostProtocol


class GitHub(_SharedAPI, _SharedOwner, PackageHostProtocol):
    """ Tools to interface a GitHub Repository.
        Todo: Get and Set GitHub repo private. """
    DEFAULT_OWNER = "ManderaGeneral"

    def __init__(self, name=None, owner=None):
        pass

    def get_version(self):
        raise NotImplementedError

    def get_date(self):
        raise NotImplementedError

    @property
    def url(self):
        return f"https://github.com/{self.owner}/{self.name}"

    @property
    def ssh_url(self):
        return f"https://Mandera:{GH_TOKEN}@github.com/{self.owner}/{self.name}.git"

    def api_url(self, endpoint=None):
        """ Get URL from owner, name and endpoint. """
        return "/".join(("https://api.github.com", "repos", self.owner, self.name) + ((endpoint, ) if endpoint else ()))

    @property
    def git_clone_command(self):
        return f"git clone ssh://git@github.com/{self.owner}/{self.name}.git"

    @property
    def pip_install_command(self):
        return f"pip install git+ssh://git@github.com/{self.owner}/{self.name}.git"

    def exists(self):
        """ Return whether this API's target exists. """
        return self._request().ok

    def download(self, path=None, version=None, overwrite=False):
        """ Clone a GitHub repo into a path, defaults to working_dir / name.
            Creates a folder with Package's name first. """
        if version:
            raise NotImplementedError

        if not self.exists():
            return Log(__name__).warning(f"Cannot download {self.name}, couldn't find on GitHub.")

        path = Path(path)
        repo_path = path / self.name

        repo_path.overwrite_check(overwrite=overwrite)

        Log(__name__).info(f"Downloading {self.name} from GitHub.")
        with path.as_working_dir():
            Terminal("git", "clone", self.url, capture_output=False)

        return path

    def get_owners_packages(self):
        """ Get a set of an owner's packages' names on GitHub. """
        # repos = requests.get(f"https://api.github.com/users/{self.owner}/repos", **self.request_kwargs()).json()  # This only gave public

        repos = requests.get(f"https://api.github.com/search/repositories?q=user:{self.owner}", **self.request_kwargs()).json()["items"]
        return set(repo["name"] for repo in repos)

    def get_website(self):
        """ Get website specified in repository details.

            :rtype: list[str] """
        return self._request(method="get").json()["homepage"]

    def set_website(self, website):
        """ Set a website for the GitHub repository.

            :rtype: requests.Response """
        return self._request(method="patch", name=self.name, homepage=website)

    def get_topics(self):
        """ Get a list of topics in the GitHub repository.

            :rtype: list[str] """
        return self._request(method="get", endpoint="topics").json()["names"]

    def set_topics(self, *topics):
        """ Set topics for the GitHub repository.

            :param str topics:
            :rtype: requests.Response """
        return self._request(method="put", endpoint="topics", names=topics)

    def get_description(self):
        """ Get a string of description in the GitHub repository.

            :rtype: list[str] """
        return self._request(method="get").json()["description"]

    def set_description(self, description):
        """ Set a description for the GitHub repository.

            :rtype: requests.Response """
        return self._request(method="patch", name=self.name, description=description)

    def request_kwargs(self):
        # return {
        #     "headers": {
        #         "Accept": "application/vnd.github.mercy-preview+json",
        #         "Authorization": f"token {GH_TOKEN.value}"
        #     },
        # }
        return {
            # "headers": {"Accept": "application/vnd.github.mercy-preview+json"},
            "headers": {
                # "Authorization": f"token {GH_TOKEN}",
                "Accept": "application/vnd.github.v3+json",
            },
            "auth": (self.owner, GH_TOKEN.value),
        }

    def _request(self, method="get", url=None, endpoint=None, **data):
        """ :rtype: requests.Response """
        method = getattr(requests, method.lower())
        kwargs = self.request_kwargs()
        if data:
            kwargs["data"] = json.dumps(data)
        if url is None:
            url = self.api_url(endpoint=endpoint)
        return method(url=url, **kwargs)















