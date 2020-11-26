

from generallibrary import initBases
from generalfile import Path




class _Repo:
    def read(self, path): """ Get string from relative path. """; raise NotImplementedError
    def read(self, path): """ Write string to document. """; raise NotImplementedError
    def read(self, path): """ Get string from relative path. """; raise NotImplementedError



@initBases
class RepoLocal(_Repo):
    def __init__(self, repo_path):
        self.repo_path = Path(repo_path).absolute()

    def read(self, path):
        """ Use generalfile to read path. """
        return (self.repo_path / path).text.read()



print(RepoLocal("A:/Programming/Python/generalpackager").read("metadata.json"))
