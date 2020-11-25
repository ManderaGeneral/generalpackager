
from generallibrary import Markdown, comma_and_and, deco_default_self_args, initBases
import pandas

from generalpackager.producer.producer import Producer


@initBases
class ProducerReadme(Producer):
    """ Contains methods to generate readme sections from arguments.
        Arguments can come from argument, or an added API instance. """

    def __init__(self, *apis):
        pass

    @deco_default_self_args
    def get_badges_markdown(self, name):
        """ Get badges markdown. """
        return Markdown(*self.get_badges_list(name=name))

    @deco_default_self_args
    def get_installation_markdown(self, name, extras_require):
        """ Get install markdown. """
        markdown = Markdown(header="Installation").add_code_lines(f'pip install {name}')

        if len(extras_require) > 1:
            rows = [{
                "Name": extra,
                "Command": f"`pip install {name}[{extra}]`",
                "Extra packages": comma_and_and(*[f"`{x}`" for x in requires], period=False),
            } for extra, requires in extras_require.items()]

            Markdown(pandas.DataFrame(rows).to_markdown(index=False), header="Extras", hashtags=4, parent=markdown)

        return markdown

    @deco_default_self_args
    def get_topics_markdown(self, topics):
        """ Get topics markdown. """
        print(topics)

    @deco_default_self_args
    def get_description_markdown(self, name, description):
        """ Get description text. """

        lines = [
            f"# Package: {name}",
            description,
        ]
        return "\n".join(lines)



    def create_readme_markdown(self):
        """ Create readme using added APIs indirectly. """
        l = [
            self.get_badges(),
            self.get_installation(),
        ]

        markdown = Markdown()
        for md in l:
            md.set_parent(markdown)
        print(markdown)














