
from generallibrary import Markdown, comma_and_and, deco_default_self_args
import pandas
from generalpackager import APILocalRepo, APIGitHub

class GeneratorReadme:
    """ Contains methods to generate readme sections from arguments.
        Arguments can come from hardcode, or an API. """

    apis_classes = APILocalRepo, APIGitHub

    def __init__(self, localRepo=None, gitHub=None):
        self.localRepo = localRepo
        self.gitHub = gitHub

    def _set_api_attributes(self):
        attrs_list = [{key: value for key in api.fetched_keys} for api in self.apis_classes]  # HERE ** Figure out how to access possibly shared attrs
        for api in self.apis_classes:


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

        return Markdown(header=None, *l)

    def get_installation(self, name, extras_require):
        """ Get install text. """
        section = Markdown()

        lines = [
            f"## Installation",
            "```",
            f'pip install {name}',
            "```",
        ]

        if len(extras_require) > 1:
            rows = [{
                "Name": extra,
                "Command": f"`pip install {name}[{extra}]`",
                "Extra packages": comma_and_and(*[f"`{x}`" for x in requires], period=False),
            } for extra, requires in extras_require.items()]

            df = pandas.DataFrame(rows)
            lines.extend(["#### Extras", df.to_markdown(index=False)])
        return "\n".join(lines)