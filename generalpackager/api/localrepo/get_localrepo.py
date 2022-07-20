
from generalpackager.api.localrepo.base import LocalRepo
from generalpackager.api.localrepo.targets.python import LocalRepo_Python


LOCALREPOS = [LocalRepo, LocalRepo_Python]


def get_localrepo(path):
    base = LocalRepo(path=path)
    if base.metadata.exists():
        for localrepo in LOCALREPOS:
            if localrepo.target == base.metadata.target:
                pass
    else:
        return base
