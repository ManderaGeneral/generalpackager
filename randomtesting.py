

from generalpackager import Packager


# print(Packager().get_ordered_packagers())


import git
repo = git.Repo(search_parent_directories=True)
sha = repo.head.object.hexsha

print(sha)
