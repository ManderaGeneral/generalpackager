
# Todo: Method to upload to PyPI.


class PyPI:
    """ Tools to interface pypi.org. """
    def __init__(self, name):
        self.name = name

        self.url = f"https://pypi.org/project/{self.name}/"

        # assert self.url 200
