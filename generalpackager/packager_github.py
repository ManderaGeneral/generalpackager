

from git import Repo


class _PackagerGitHub:
    """ Sync metadata. """
    def sync_github_metadata(self):
        """ Sync GitHub with local metadata.

            :param generalpackager.Packager self: """
        self.github.set_website(self.pypi.url)
        self.github.set_description(self.localrepo.description)
        self.github.set_topics(*self.get_topics())

    def clone_repo(self, url=None, path=None):
        """ Clone a GitHub repo into a path to produce a LocalRepo.

            :param generalpackager.Packager self:
            :param url:
            :param path: """
        if url is None:
            url = self.github.url
        if path is None:
            path = self.path

        Repo.clone_from(url=url, to_path=path)














