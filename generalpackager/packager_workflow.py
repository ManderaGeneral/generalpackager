
from generalfile import Path
from generallibrary import EnvVar, Log


class _PackagerWorkflow:
    def run_ordered_methods(self, *funcs):
        """ :param generalpackager.Packager self: """
        order = self.get_ordered_packagers()
        for func in funcs:
            for packager in order:
                func(packager)

    def workflow_unittest(self):
        """ :param generalpackager.Packager self: """
        Log().debug("Working dir for workflow_unittest:", Path().absolute())

        self.run_ordered_methods(
            lambda packager: packager.generate_localfiles(include_aesthetic=False),
            lambda packager: packager.localrepo.unittest(),
        )

    def workflow_sync(self):
        """ Runs in workflow once Packagers have created each LocalRepo from latest master commit.
            Todo: Add single job to make sure workflow is up to date.
            It can generate new workflow, compare, and then stop workflow after commiting and pushing.

            :param generalpackager.Packager self: """
        trigger_repo = str(EnvVar('GITHUB_REPOSITORY')).split('/')[1]
        msg1 = f"[CI AUTO] Sync triggered by {trigger_repo}"
        msg2 = f"[CI AUTO] Publish triggered by {trigger_repo}"

        # Log().configure_stream()

        self.run_ordered_methods(
            lambda packager: packager.if_publish_bump(),
            lambda packager: packager.generate_localfiles(include_aesthetic=False),
            lambda packager: packager.localrepo.unittest(),  # Will set coverage percentage
            lambda packager: packager.generate_localfiles(include_aesthetic=True),  # With coverage number
            lambda packager, msg=msg1: packager.commit_and_push(message=msg, tag=False),
            lambda packager, msg=msg2: packager.if_publish_publish(message=msg),
            lambda packager: packager.sync_github_metadata(),
        )

        for packager in self.summary_packagers():
            packager.upload_package_summary(msg=msg1)

    def upload_package_summary(self, msg):
        """ :param generalpackager.Packager self: """
        self.org_readme_file.generate()
        self.commit_and_push(message=msg)

    def if_publish_bump(self):
        """ Bump if updated and any other Packager is bumped.

            :param generalpackager.Packager self: """
        if self.general_bumped_set() and not self.is_bumped() and self.compare_local_to_pypi(aesthetic=False):
            self.localrepo.bump_version()

    def if_publish_publish(self, message):
        """ Only does anything if bumped.
            Generate new readme, commit and push with tag.
            Upload to PyPI unless private.
            Upload exe if exetarget.py exists.

            :param generalpackager.Packager self:
            :param message: """
        if self.is_bumped():
            self.readme_file.generate()
            self.commit_and_push(message=message, tag=True)
            if not self.localrepo.metadata.private:
                self.localrepo.upload()
            # if self.localrepo.get_exetarget_path().exists():
            #     self.localrepo.generate_exe()
            #     MainframeClient().upload_exe(exe_path=self.localrepo.get_exeproduct_path(), name=self.name, version=self.localrepo.metadata.version)








