
import requests
import re


class PyPI:
    """ Tools to interface pypi.org """
    def __init__(self, name):
        self.name = name

        self.url = f"https://pypi.org/project/{self.name}/"

    def get_users_packages(self, user="Mandera"):
        """ Get a list of a user's packages' names on PyPI. """
        return re.findall("/project/(.*)/", requests.get(f"https://pypi.org/user/{user}/").text)

