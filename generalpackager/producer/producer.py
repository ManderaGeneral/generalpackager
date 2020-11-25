
from generallibrary import deco_default_self_args


class Producer:
    """ Contains generic methods for Producers. """
    def __init__(self, *apis):
        self.load_api_instance(*apis)

    def load_api_instance(self, *apis):
        """ Load an API instance's attrs into this Producer instance.
            These attributes are used automatically by `@deco_default_self_args`. """
        for api in apis:
            for key, value in api.get_api_attrs().items():
                assert value is not ...
                self_value = getattr(self, key, None)
                if self_value is not None and self_value != value:
                    raise AttributeError(f"API {api} {key} mismatch: {value} != {self_value}")

                setattr(self, key, value)

    @deco_default_self_args
    def get_badges_list(self, name):
        """ Get badges list. """
        pypi_version = "[![PyPI version shields.io](https://img.shields.io/pypi/v/PACKAGE.svg)](https://pypi.org/project/PACKAGE/)"
        python_version = "[![PyPI pyversions](https://img.shields.io/pypi/pyversions/PACKAGE.svg)](https://pypi.python.org/pypi/PACKAGE/)"
        platforms = "[![Generic badge](https://img.shields.io/badge/platforms-Windows%20|%20Ubuntu%20|%20MacOS-blue.svg)](https://shields.io/)"
        workflow = "[![workflow Actions Status](https://github.com/ManderaGeneral/PACKAGE/workflows/workflow/badge.svg)](https://github.com/ManderaGeneral/PACKAGE/actions)"
        lgtm_alerts = "[![Total alerts](https://img.shields.io/lgtm/alerts/g/ManderaGeneral/PACKAGE.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ManderaGeneral/PACKAGE/alerts/)"

        l = [
            pypi_version,
            python_version,
            platforms,
            workflow,
            lgtm_alerts,
        ]
        return [badge.replace("PACKAGE", name) for badge in l]