
import requests
import re


class PyPI:
    """ Tools to interface pypi.org
        Todo: get_latest_version() """
    def __init__(self, name):
        self.name = name

        self.url = self.get_url(name=self.name)

    @classmethod
    def is_creatable(cls, name):
        """ Return whether this API can be created. """
        return requests.get(url=cls.get_url(name=name)).status_code == 200

    @staticmethod
    def get_url(name):
        """ Get static URL from owner and name. """
        return f"https://pypi.org/project/{name}/"

    @staticmethod
    def get_users_packages(user=None):
        """ Get a set of a user's packages' names on PyPI. """
        if user is None:
            user = "Mandera"
        return set(re.findall("/project/(.*)/", requests.get(f"https://pypi.org/user/{user}/").text))









































