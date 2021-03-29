
from generalpackager.api.local_repo import LocalRepo

from git import Repo


class _PackagerGitHub:
    """ Sync metadata. """
    def __init__(self):
        self.commit_sha = "master"

    def sync_github_metadata(self):
        """ Sync GitHub with local metadata.

            :param generalpackager.Packager self: """
        self.github.set_website(self.pypi.url)
        self.github.set_description(self.localrepo.description)
        self.github.set_topics(*self.get_topics())

    def clone_repo(self, path=None):
        """ Clone a GitHub repo into a path to produce a LocalRepo.

            :param generalpackager.Packager self:
            :param path: """
        if path is None:
            path = self.path
        Repo.clone_from(url=self.github.url, to_path=path)
        return LocalRepo(self.name)

    def commit_push_store_sha(self, message, tag=False):
        """ Use LocalRepos method commit_and_push but also store short sha1.

            :param generalpackager.Packager self:
            :param message:
            :param tag: """
        self.commit_sha = self.localrepo.commit_and_push(message=message, tag=tag, owner=self.github.owner)













