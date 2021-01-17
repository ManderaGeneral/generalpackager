
import requests
import re


class PyPI:
    """ Tools to interface pypi.org """
    def __init__(self, name):
        self.name = name

        self.url = f"https://pypi.org/project/{self.name}/"

    @staticmethod
    def get_users_packages(user=None):
        """ Get a set of a user's packages' names on PyPI. """
        if user is None:
            user = "Mandera"
        return set(re.findall("/project/(.*)/", requests.get(f"https://pypi.org/user/{user}/").text))










































