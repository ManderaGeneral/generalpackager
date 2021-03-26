
from generalpackager.api.shared import _SharedAPI
from generallibrary import Ver, Date, Recycle
from generalfile import Path

import requests
import re


def download(url, path):
    """ Todo: Move download to it's own package. """
    data = requests.get(url)
    if data.status_code != 200:
        raise AttributeError(f"Request for url {url} did not yield a status code of 200.'")

    path = Path(path)

    with path.lock():
        path.get_parent().create_folder()
        with open(str(path), "wb") as file:
            file.write(data.content)
    return path


class PyPI(Recycle, _SharedAPI):
    """ Tools to interface pypi.org """
    _recycle_keys = {"name": str, "owner": str}

    def __init__(self, name=None, owner=None):
        if name is None:
            name = "generalpackager"
        if owner is None:
            owner = "Mandera"
        self.name = name
        self.owner = owner

        self.url = f"https://pypi.org/project/{self.name}/"

    def exists(self):
        """ Return whether this API's target exists. """
        return requests.get(url=self.url).status_code == 200

    def get_tarball_url(self, version=None):
        """ Get URL to download tarball. """
        if version is None:
            version = self.get_version()
        return f"https://pypi.io/packages/source/{self.name[0]}/{self.name}/{self.name}-{version}.tar.gz"

    def download_and_unpack_tarball(self, target_folder, version=None, overwrite=False):
        """ Download tar ball to cache, extract it, remove tar ball.
            Returns target folder tarball is extracted in. """
        target_folder = Path(target_folder)
        temp = Path.get_cache_dir() / "Python/temp.tar.gz"
        download(self.get_tarball_url(version=version), path=temp)
        temp.unpack(base=target_folder, overwrite=overwrite)
        temp.delete(error=False)
        return target_folder

    def get_owners_packages(self):
        """ Get a set of a owner's packages' names on PyPI. """
        return set(re.findall("/project/(.*)/", requests.get(f"https://pypi.org/user/{self.owner}/").text))

    def get_version(self):
        """ Get version of latest publish on PyPI.
            Todo: Find a faster fetch for latest PyPI version. """
        return Ver(re.findall(f"{self.name} ([.0-9]+)\n", requests.get(self.url).text)[0])

    def get_date(self):
        """ Get datetime of latest release.
            Todo: Find a faster fetch for latest PyPI datetime. """
        return Date(re.findall('Generated (.+) for commit', requests.get(self.url).text)[0])

    def reserve_name(self):
        pass


























