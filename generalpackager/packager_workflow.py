
from generallibrary import CodeLine, comma_and_and


class _PackagerWorkflow:
    """ Afraid to start handling all the logic, might not be worth the time. """
    @staticmethod
    def _var(string):
        return f"${{{{ {string} }}}}"

    @staticmethod
    def _commit_msg_if(**conditions):
        checks = [f"contains(github.event.head_commit.message, '[CI {key}]') == {str(value).lower()}" for key, value in conditions.items()]
        return f"if: {' && '.join(checks)}"

    _commit_message = "github.event.head_commit.message"
    _action_checkout = "actions/checkout@v2"
    _action_setup_python = "actions/setup-python@v2"
    _matrix_os = "matrix.os"
    _matrix_python_version = "matrix.python-version"

    def __init__(self):
        self._secrets_token = self._var('secrets.ACTIONS_TOKEN')

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
            step.add(codeline)
        return step

    def step_checkout(self):
        """ :param generalpackager.Packager self: """
        return self.get_step("Checkout repository.", "uses: actions/checkout@v2")

    def step_setup_python(self, version):
        """ :param generalpackager.Packager self:
            :param version: """
        with_ = CodeLine("with:")
        with_.add(f"python-version: {version}")
        return self.get_step(f"Set up python version {version}", f"uses: {self._action_setup_python}", with_)

    def step_install_package(self, *extra_packages):
        """ :param generalpackager.Packager self: """
        packages = {".[full]", "wheel"}.union(extra_packages)
        run = CodeLine("run: |")
        run.add("python -m pip install --upgrade pip")
        run.add(f"pip install {' '.join(packages)}")
        return self.get_step(f"Install packages {comma_and_and(*packages)}", run)

    def step_run_unittests(self):
        """ :param generalpackager.Packager self: """
        run = CodeLine("run: |")
        env_vars = " ".join([f"{env_var.name}={env_var.actions_name}" for env_var in self.localmodule.get_env_vars() if env_var.actions_name])
        run.add(f"python generalpackager/test/main.py {env_vars}")
        return self.get_step(f"Run unittests.", run)

    def step_sync(self):
        """ :param generalpackager.Packager self: """
        run = CodeLine("run: |")
        run.add(f"python")
        run.add(f"from generalpackager import Packager")
        run.add(f"packager = Packager('{self.name}')")
        run.add(f"packager.generate_localfiles()")
        run.add(f'packager.commit_and_push("[CI SYNC] {self._var(self._commit_message)}")')
        run.add(f"packager.sync_github_metadata()")
        run.add(f"exit()")

        return self.get_step(f"Generate files, commit them and send requests to GitHub.", run)

    def get_sync_job(self):
        """ :param generalpackager.Packager self: """
        top = CodeLine("sync:")
        top.add(self._commit_msg_if(SKIP=False, SYNC=False))
        top.add(f"runs-on: ubuntu-latest")

        steps = top.add("steps:")
        steps.add(self.step_checkout())
        steps.add(self.step_setup_python(version=self.python[0]))
        steps.add(self.step_install_package("generalpackager"))
        steps.add(self.step_sync())

        return top

    def get_unittest_job(self):
        """ :param generalpackager.Packager self: """
        top = CodeLine("unittest:")
        top.add(self._commit_msg_if(SKIP=False, SYNC=True))
        top.add(f"runs-on: {self._var(self._matrix_os)}")

        strategy = top.add("strategy:")
        matrix = strategy.add("matrix:")
        matrix.add(f"python-version: {list(self.python)}".replace("'", ""))
        matrix.add(f"os: {[f'{os}-latest' for os in self.os]}".replace("'", ""))

        steps = top.add("steps:")
        steps.add(self.step_checkout())
        steps.add(self.step_setup_python(version=self._var(self._matrix_python_version)))
        steps.add(self.step_install_package())
        steps.add(self.step_run_unittests())

        return top







