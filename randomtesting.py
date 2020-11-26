
import generallibrary
from generalpackager import *
from generalfile import Path

from pprint import pprint




class _Repo:
    pass

@initBases
class RepoGitHub(_Repo):










repoLocal = RepoLocal("A:/Programming/Python/generalpackager")
repoPypi = RepoPypi("generalpackager", "0.6.2")
repoGitHub = RepoGitHub("ManderaGeneral", "generallibrary")





repoGitHub.set_topics(repoLocal.topics)

















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














