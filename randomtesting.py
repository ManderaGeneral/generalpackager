
import generallibrary
from generalpackager import *
from generalfile import Path

from pprint import pprint




packager = Packager("A:/Programming/Python/generallibrary")


packager.generate_readme()

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


# HERE ** Create method to update topics to what's in PS


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














