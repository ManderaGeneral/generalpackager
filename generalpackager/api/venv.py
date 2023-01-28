import sys

from generalfile import Path
from generallibrary import deco_cache, Ver, Terminal, debug, EnvVar, remove, DecoContext, deco_require



class Venv(DecoContext):
    """ Todo: Ensure handling of no active venv. """
    PATH = EnvVar("PATH")
    VIRTUAL_ENV = EnvVar("VIRTUAL_ENV", default=None)

    def __init__(self, path=None):
        if path is None:
            path = Path.get_active_venv_path()
        self.path = Path(path)
        self.previous_venv = None

    def before(self, *args, **kwargs):
        self.previous_venv = self.activate()

    def after(self, *args, **kwargs):
        self.previous_venv.activate()

    def pyvenv_cfg_path(self):  return self.path / "pyvenv.cfg"
    def scripts_path(self):     return self.path / "Scripts"
    def python_exe_path(self):  return self.path / "Scripts/python.exe"
    def site_packages_path(self):  return self.path / "Lib/site-packages"
    def python_home_path(self): return Path(self.cfg()["home"])

    def exists(self):
        return self.path.is_venv()

    def active(self):
        return Path.get_active_venv_path() is self.path

    def create_venv(self):
        assert self.path.empty()
        Terminal("-m", "venv", self.path, python=True)

    def remove_active_venv(self):
        active_venv = Venv()
        self.PATH.value = ";".join([path for path in self.PATH.value.split(";") if active_venv.scripts_path() != Path(path)])
        remove(sys.path, str(active_venv.scripts_path()))
        remove(sys.path, str(active_venv.site_packages_path()))

    @deco_require(exists)
    def activate(self):
        active_venv = Venv()
        if active_venv.path is not self.path:
            self.remove_active_venv()

            sys.path = [str(self.path), str(self.site_packages_path())] + sys.path
            self.PATH.value = f"{self.scripts_path()};{self.PATH}"
            self.VIRTUAL_ENV.value = self.path
            sys.prefix = self.path
            sys.executable = self.python_exe_path()
        return active_venv

    @deco_require(exists)
    def upgrade(self):
        with self:
            return Terminal("-m", "ensurepip", "--upgrade", python=True).string_result

    @deco_require(exists)
    @deco_cache()
    def cfg(self):
        r""" Example: https://github.com/ManderaGeneral/generalpackager/issues/57#issuecomment-1399402211 """
        return self.pyvenv_cfg_path().cfg.read()

    def python_version(self):
        return Ver(self.cfg().get("version") or self.cfg().get("version_info"))

    @classmethod
    def list_venv_paths(cls, path=None):
        active_venv_path = Path.get_active_venv_path()
        if path is None and active_venv_path:
            path = active_venv_path.get_parent()
        else:
            path = Path(path)
        return path.get_children(filt=lambda p: p.is_venv())

    @staticmethod
    def debug():
        import os
        import sys

        debug(locals(),
              "os.environ['PATH']",
              "os.environ['VIRTUAL_ENV']",
              "sys.prefix",
              "sys.path",
              "sys.executable",
              )

