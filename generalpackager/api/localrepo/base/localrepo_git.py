
from generallibrary import deco_cache
from generalfile import Path
from git import Repo
import re


class _LocalRepo_Git:
    def get_commit_message(self):
        """ :param generalpackager.LocalRepo self: """
        return self.commit_editmsg_file.path.text.read()

    @property
    @deco_cache()
    def repo(self):
        """ :param generalpackager.LocalRepo self: """
        return Repo(str(self.path))

    def commit(self, message=None):
        """ :param generalpackager.LocalRepo self: """
        self.repo.git.add(A=True)
        self.repo.index.commit(message=str(message) if message else "No commit message.")

    @property
    def commit_sha(self):
        """ :param generalpackager.LocalRepo self: """
        return self.repo.head.object.hexsha

    @property
    def commit_sha_short(self):
        """ :param generalpackager.LocalRepo self: """
        return self.commit_sha[0:8]

    def git_changed_files(self):
        """ Get a list of relative paths changed files using local .git folder.

            :param generalpackager.LocalRepo self: """
        return [Path(file) for file in re.findall("diff --git a/(.*) " + "b/", self.repo.git.diff())]






























