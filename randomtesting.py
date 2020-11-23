
import generallibrary
from generalpackager import *
from generalfile import Path


repoMarkdown = RepoMarkdown("A:/Programming/Python/generalpackager")
# repoMarkdown = RepoMarkdown("A:/Programming/Python/generallibrary")



repoMarkdown.create_readme([
    repoMarkdown.get_badges(),
    repoMarkdown.get_description(),
    repoMarkdown.get_install(),
    repoMarkdown.get_attributes(),
    repoMarkdown.get_todos(),
])





