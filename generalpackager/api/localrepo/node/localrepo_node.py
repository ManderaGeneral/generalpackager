from generallibrary import Terminal, Log
from generalpackager.api.localrepo.base.localrepo import LocalRepo
from generalpackager.api.localrepo.node.metadata_node import Metadata_Node


class LocalRepo_Node(LocalRepo):
    _cls_target = LocalRepo.Targets.node
    _cls_metadata = Metadata_Node

    def run_tests(self):
        with self.path.as_working_dir():
            Terminal("jest", capture_output=False)

    def _stall(self, local, editable, create, remove):
        cmd = create if editable else remove
        G = "-G"
        args = ["npm", cmd, G, self.name]
        if local:
            args.remove(G)

        Log(__name__).debug(f"{cmd} for {self.name}")

        with self.path.as_working_dir():
            Terminal(*args, capture_output=False)

    def install(self, local=True, editable=False):
        self._stall(local=local, editable=editable, create="install", remove="uninstall")

    def uninstall(self, local=True, editable=False):
        self._stall(local=local, editable=editable, create="link", remove="unlink")

    def publish(self, public=True):
        Log(__name__).debug(f"Publish for {self.name}")

        with self.path.as_working_dir():
            Terminal("npm", "publish", capture_output=False)



















