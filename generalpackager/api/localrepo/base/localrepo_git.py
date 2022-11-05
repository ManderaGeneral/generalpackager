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

    @deco_path_as_working_dir
    def commit(self, message=None):
        """ :param generalpackager.LocalRepo self: """
        if message is None:
            message = "No commit message"
        terminal("git", "commit", "-a", "-m", message, "--author", f"{self.RUNNER_NAME} {self.RUNNER_EMAIL}")

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






























