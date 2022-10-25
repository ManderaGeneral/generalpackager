

class _LocalRepo_Git:
    def get_commit_message(self):
        """ :param generalpackager.Packager self: """
        return self.commit_editmsg_file.path.text.read()

