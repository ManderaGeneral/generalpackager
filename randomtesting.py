

from generalpackager import Packager


# print(Packager().get_ordered_packagers())


import git
repo = git.Repo(search_parent_directories=True)
sha = repo.head.object.hexsha

print(sha)

# 35a9475a68ad470f897c940516fad05152c1fd2a