
from generallibrary import Markdown, comma_and_and, deco_default_self_args
import pandas


class GeneratorReadme:
    """ Contains methods to generate readme sections from arguments.
        Arguments can come from argument, or an added API instance. """

    def __init__(self, *apis):
        self._apis = []
        for api in apis:
            self.add_api_instance(api)

    def add_api_instance(self, api):
        """ Add an api instance to load it's attrs into this instance.
            These attributes are used automatically by `@deco_default_self_args`. """
        for key, value in api.get_api_attrs().items():
            self_value = getattr(self, key, None)
            if self_value is not None and self_value != value:
                raise AttributeError(f"API {api} {key} mismatch: {value} != {self_value}")
            setattr(self, key, value)

    @deco_default_self_args
    def get_badges(self, name):
        """ Get list of badge images. """
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
        l = [badge.replace("PACKAGE", name) for badge in l]

        return Markdown(*l)

    @deco_default_self_args
    def get_installation(self, name, extras_require):
        """ Get install text. """
        markdown = Markdown(header="Installation").add_code_lines(f'pip install {name}')

        if len(extras_require) > 1:
            rows = [{
                "Name": extra,
                "Command": f"`pip install {name}[{extra}]`",
                "Extra packages": comma_and_and(*[f"`{x}`" for x in requires], period=False),
            } for extra, requires in extras_require.items()]

            Markdown(pandas.DataFrame(rows).to_markdown(index=False), header="Extras", hashtags=4, parent=markdown)

        return markdown

    def create_readme(self):
        """ Create readme using added APIs. """
        markdown = Markdown()
        self.get_badges().set_parent(markdown)
        self.get_installation().set_parent(markdown)
        print(markdown)














