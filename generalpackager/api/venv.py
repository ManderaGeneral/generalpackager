from generalfile import Path
from generallibrary import deco_cache, Ver


class Venv:
    def __init__(self, path):
        self.path = Path(path)

    def pyvenv_cfg_path(self):
        return self.path / "pyvenv.cfg"

    @deco_cache()
    def cfg(self):
        """ Example:
            {'base-exec-prefix': 'C:\\Users\\ricka\\AppData\\Local\\Programs\\Python\\Python311',
            'base-executable': 'C:\\Users\\ricka\\AppData\\Local\\Programs\\Python\\Python311\\python.exe',
            'base-prefix': 'C:\\Users\\ricka\\AppData\\Local\\Programs\\Python\\Python311',
            'home': 'C:\\Users\\ricka\\AppData\\Local\\Programs\\Python\\Python311',
            'implementation': 'CPython',
            'include-system-site-packages': False,
            'version_info': '3.11.0.final.0',
            'virtualenv': '20.16.4'} """
        return self.pyvenv_cfg_path().cfg.read()

    def python_path(self):
        return self.cfg()["home"]

    def python_version(self):
        return Ver(self.cfg()["version_info"])

    def virtualenv_version(self):
        return Ver(self.cfg()["virtualenv"])


