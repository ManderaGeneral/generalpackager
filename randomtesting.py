
import generallibrary
from generalpackager import *
from generalfile import Path


from pprint import pprint

gitHub = GitHub("ManderaGeneral", "generallibrary")
topics = gitHub.get_topics()

print(topics)
topics.append("hi")

result = gitHub.set_topics(topics)
print(result.json())



repoMarkdown = RepoMarkdown("A:/Programming/Python/generalpackager")
# repoMarkdown = RepoMarkdown("A:/Programming/Python/generallibrary")



# repoMarkdown.create_readme([
#     repoMarkdown.get_badges(),
#     repoMarkdown.get_description(),
#     repoMarkdown.get_install(),
#     repoMarkdown.get_attributes(),
#     repoMarkdown.get_todos(),
# ])





