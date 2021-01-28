
from generallibrary import CodeLine, comma_and_and
from generalfile import Path


class _PackagerWorkflow:
    """ Afraid to start handling all the logic, might not be worth the time. """
    @staticmethod
    def _var(string):
        return f"${{{{ {string} }}}}"

    @staticmethod
    def _commit_msg_if(**conditions):
        checks = [f"contains(github.event.head_commit.message, '[CI {key}]') == {str(value).lower()}" for key, value in conditions.items()]
        return f"if: {' && '.join(checks)}"

    _commit_msg = "github.event.head_commit.message"
    _action_checkout = "actions/checkout@v2"
    _action_setup_python = "actions/setup-python@v2"
    _matrix_os = "matrix.os"
    _matrix_python_version = "matrix.python-version"

    def get_triggers(self):
        """ :param generalpackager.Packager self: """
        on = CodeLine("on:")
        push = on.add("push:")
        branches = push.add("branches:")
        branches.add("- master")
        return on

    def get_step(self, name, *codelines):
        """ . """
        step = CodeLine(f"- name: {name}")
        for codeline in codelines:
            if codeline:
                step.add(codeline)
        return step

    def step_checkout(self):
        """ Todo: Add token here to see if we can trigger workflow for dependents auto testing.
            https://github.com/actions/checkout

            :param generalpackager.Packager self: """
        return self.get_step("Checkout repository", "uses: actions/checkout@v2")

    def step_setup_python(self, version):
        """ :param generalpackager.Packager self:
            :param version: """
        with_ = CodeLine("with:")
        with_.add(f"python-version: {version}")
        return self.get_step(f"Set up python version {version}", f"uses: {self._action_setup_python}", with_)

    def step_install_necessities(self):
        """ :param generalpackager.Packager self: """
        run = CodeLine("run: |")
        run.add("python -m pip install --upgrade pip")
        run.add(f"pip install setuptools wheel twine")
        return self.get_step(f"Install necessities pip, setuptools, wheel, twine", run)

    def step_install_package_pip(self, *packages):
        """ Supply package name as it's stated on pypi.

            :param generalpackager.Packager self: """
        run = CodeLine(f"run: pip install {' '.join(packages)}")
        return self.get_step(f"Install pip packages {comma_and_and(*packages, period=False)}", run)

    def step_install_package_git(self, *author_repo):
        """ Supply author/repo, e.g. ManderaGeneral/generalpackager

            :param generalpackager.Packager self: """
        assert all(map(lambda x: "/" in x, author_repo))

        run = CodeLine(f"run: pip install {' '.join([f'git+https://github.com/{pkg}.git' for pkg in author_repo])}")
        return self.get_step(f"Install git repos {comma_and_and(*author_repo, period=False)}", run)

    def get_env(self):
        """ :param generalpackager.Packager self: """
        env = CodeLine("env:")
        for env_var in self.localmodule.get_env_vars():
            if env_var.actions_name:
                env.add(f"{env_var.name}: {env_var.actions_name}")
        if not env.get_children():
            return None
        return env

    def step_unittests(self):
        """ :param generalpackager.Packager self: """
        run = f"run: python -m unittest discover {self.name}/{self.name}/test"
        return self.get_step(f"Run unittests for {self.name}", run, self.get_env())

    def step_sync(self):
        """ :param generalpackager.Packager self: """
        msg = f"[CI SYNC]"
        run = f'run: python -c "from generalpackager import Packager; Packager(\'{self.name}\', commit_sha=\'{self._var("github.sha")}\').sync_package(\'{msg}\')"'
        return self.get_step(f"Sync", run, self.get_env())

    def step_publish(self):
        """ :param generalpackager.Packager self: """
        run = f'run: python -c "from generalpackager import Packager; Packager(\'{self.name}\').localrepo.upload()"'
        return self.get_step(f"Publish", run, self.get_env())

    def get_unittest_job(self):
        """ :param generalpackager.Packager self: """
        top = CodeLine("unittest:")
        top.add(self._commit_msg_if(NOTEST=False))
        top.add(f"runs-on: {self._var(self._matrix_os)}")

        strategy = top.add("strategy:")
        matrix = strategy.add("matrix:")
        matrix.add(f"python-version: {list(self.python)}".replace("'", ""))
        matrix.add(f"os: {[f'{os}-latest' for os in self.os]}".replace("'", ""))

        steps = top.add("steps:")
        steps.add(self.step_setup_python(version=self._var(self._matrix_python_version)))
        steps.add(self.step_install_necessities())

        for packager in self.get_ordered_packagers():
            steps.add(self.step_install_package_git(f"{packager.github.owner}/{packager.name}"))

        steps.add(self.step_grp_clone())

        # for packager in self.get_ordered_packagers():
        #     steps.add(packager.step_unittests())

        # steps.add(self.step_install_necessities())
        # steps.add(self.step_install_package_git(".[full]"))
        # steps.add(self.step_unittests())

        return top

    def get_sync_push_publish_job(self):
        """ :param generalpackager.Packager self: """
        top = CodeLine("sync_and_publish:")
        top.add("needs: unittest")
        top.add(self._commit_msg_if(SKIP=False))
        top.add(f"runs-on: ubuntu-latest")

        steps = top.add("steps:")
        steps.add(self.step_checkout())
        steps.add(self.step_setup_python(version=self.python[0]))
        steps.add(self.step_install_necessities())
        steps.add(self.step_install_package_pip(".[full]"))
        steps.add(self.step_install_package_pip(*sorted(self.get_users_package_names())))
        steps.add(self.step_sync())
        steps.add(self.step_publish())

        return top

    def step_grp_clone(self):
        """ :param generalpackager.Packager self: """
        run = CodeLine(f'run: |')

        run.add('python -c "from generalpackager import Packager; Packager(\'generalpackager\', \'\').workflow_stuff()"')

        return self.get_step(f"Clone all repos", run, self.get_env())

    def workflow_stuff(self):
        """ :param generalpackager.Packager self: """
        self.load_general_packagers()
        order = self.get_ordered_packagers()

        for packager in order:
            packager.generate_localfiles(aesthetic=False)
            print(packager.name, "sync")

        for packager in order:
            packager.localrepo.pip_install()
            print(packager.name, "install")

        for packager in order:
            packager.localrepo.unittest()
            print(packager.name, "install")


        # from generalfile import Path
        # Path().view()

        # HERE ** Install because of tests' dependencies using install not repo

        # for packager in order:
        #     print(packager.name, "install")
        #     packager.localrepo.pip_install()





