
import generallibrary
from generalpackager import *
from generalfile import Path



repoMarkdown = RepoMarkdown("A:/Programming/Python/generalpackager")

repoMarkdown.create_readme([
    repoMarkdown.get_badges(),
    repoMarkdown.get_description(),  # HERE ***
    repoMarkdown.get_install(),
    repoMarkdown.get_attributes(),
])
