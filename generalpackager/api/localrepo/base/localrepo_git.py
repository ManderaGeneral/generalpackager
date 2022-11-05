from generallibrary import terminal
from generalfile import Path

from generalpackager.api.shared.decos import deco_path_as_working_dir


class _LocalRepo_Git:
    # https://github.com/actions/checkout/issues/13#issuecomment-724415212
    RUNNER_NAME = "github-actions[bot]"
    RUNNER_EMAIL = "<41898282+github-actions[bot]@users.noreply.github.com>"

    def commit_message(self):
        """ :param generalpackager.LocalRepo self: """
        return self.commit_editmsg_file.path.text.read()

    @deco_path_as_working_dir
    def init(self):
        """ :param generalpackager.LocalRepo self: """
        terminal("git", "init")

    @staticmethod
    def git_missing_credentials(exception):
        return "Please tell me who you are." in str(exception)

    @staticmethod
    def git_nothing_to_commit(exception):
        return "Your branch is up to date with" in str(exception)

    def git_config(self):
        """ :param generalpackager.LocalRepo self: """
        terminal("git", "config", "--global", "user.name", self.RUNNER_NAME)
        terminal("git", "config", "--global", "user.email", self.RUNNER_EMAIL)

    @deco_path_as_working_dir
    def commit(self, message=None, _recurse=True):
        """ Tries to commit. If credentials are missing then it sets them and tries once more.

            :param generalpackager.LocalRepo self: """
        try:
            terminal("git", "commit", "-a", "-m", message or "No commit message")
        except ChildProcessError as exception:
            if self.git_nothing_to_commit(exception=exception):
                return False
            elif _recurse and self.git_missing_credentials(exception=exception):
                self.git_config()
                return self.commit(message=message, _recurse=False)
            else:
                raise
        return True

    @deco_path_as_working_dir
    def push(self, url, tag=None):
        if tag is not None:
            terminal("git", "tag", tag)
            tag = ("tag", tag)

        terminal("git", "remote", "add", "origin", url)
        terminal("git", "push", "-u", "origin", "master", *tag)

    @deco_path_as_working_dir
    def clone(self, url):
        terminal("git", "clone", url)

    @deco_path_as_working_dir
    def commit_sha(self):
        """ Defaults to 'master' if missing.

            :param generalpackager.LocalRepo self: """
        return terminal("git", "rev-parse", "--verify", "HEAD", default="master")

    def commit_sha_short(self):
        """ Defaults to 'master' if missing.

            :param generalpackager.LocalRepo self: """
        return self.commit_sha()[0:8]

    @deco_path_as_working_dir
    def changed_files(self):
        """ :param generalpackager.LocalRepo self: """
        ls_files = terminal("git", "ls-files", "--modified")
        return [Path(file) for file in ls_files.splitlines()]






























