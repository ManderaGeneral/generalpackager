
from generallibrary import TreeDiagram
import generallibrary
from generalpackager import *
from generalfile import Path

from pprint import pprint

"""
Would be nice not having to install a repo package to use methods.
    Instead of using get_lines on an imported module we can read python files as text.

Moving markdown methods from Packager and removing parent argument.
Having attribute documenation in readme might actually be pretty nice, makes looking in commit history easier for one.
"""




# TreeDiagram(parent=TreeDiagram()).get_parent().view(custom_repr=lambda x: "hello\nthere")




packager = Packager("generalpackager")

packager.setup_all()
# print(packager.metadata.get_classifiers())





# packager.generate_readme()

# ps = (repo.path / "package_specific.cfg").cfg.read()
# ps = (repo.path / "metadata.json").write(ps["setup"], overwrite=True)
# print(ps)


# gitHub = GitHub("ManderaGeneral", "generallibrary")
# print(gitHub.get_description())
# print(gitHub.get_topics())
# gitHub.set_topics(gitHub.get_topics() + ["foobar"])
# gitHub.set_description("tesing")









# gitHub = APIGitHub("ManderaGeneral", "generallibrary")
# topics = gitHub.get_topics()
#
# print(topics)
# topics.append("hi")
#
# result = gitHub.set_topics(topics)
# print(result.json())


# apiLocalRepo = APILocalRepo("A:/Programming/Python/generalpackager")
# apiGitHub = APIGitHub("ManderaGeneral", "generallibrary")
# generatorReadme = ProducerReadme(apiLocalRepo, apiGitHub)



# generatorReadme.create_readme()
# generatorReadme.get_topics()

# localRepo = APILocalRepo("A:/Programming/Python/generallibrary")

# localRepo.create_readme([
#     localRepo.get_badges(),
#     localRepo.get_description(),
#     localRepo.get_install(),
#     localRepo.get_attributes(),
#     localRepo.get_todos(),
# ])














