from generalfile import Path


class Venv:
    def __init__(self, path):
        self.path = Path(path)

    def pyvenv_cfg_path(self):
        return self.path / "pyvenv.cfg"

    def python_path(self):
        return self.pyvenv_cfg_path().cfg.read()



