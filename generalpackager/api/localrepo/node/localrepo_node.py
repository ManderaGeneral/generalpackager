from typing import List

from generallibrary import Terminal, Log, VerInfo, deco_require
from generalpackager.api.localrepo.base.localrepo import LocalRepo
from generalpackager.api.localrepo.node.metadata_node import Metadata_Node


class LocalRepo_Node(LocalRepo):
    _cls_target = LocalRepo.Targets.node
    _cls_metadata = Metadata_Node

    NPM_cmd = "npm.cmd" if VerInfo().windows else "npm"

    def run_tests(self):
        with self.path.as_working_dir():
            Terminal("jest", capture_output=False)

    def _stall(self, local, editable, normal_cmd, editable_cmd):
        cmd = editable_cmd if editable else normal_cmd
        G = "-g"
        args = [self.NPM_cmd, cmd, G, self.name]
        if local:
            args.remove(G)

        Log(__name__).debug(f"{cmd} for {self.name}")

        with self.path.as_working_dir():
            Terminal(*args, capture_output=False)

    @deco_require(LocalRepo.exists)
    def install(self, local=True, editable=False):
        self._stall(local=local, editable=editable, normal_cmd="install", editable_cmd="link")

    @deco_require(LocalRepo.exists)
    def uninstall(self, local=True, editable=False):
        self._stall(local=local, editable=editable, normal_cmd="uninstall", editable_cmd="unlink")

    @deco_require(LocalRepo.exists)
    def publish(self, public=True):
        Log(__name__).debug(f"Publish for {self.name}")

        with self.path.as_working_dir():
            Terminal(self.NPM_cmd, "publish", capture_output=False)

    def list_packages(self, local=True, editable=None) -> List[str]:
        pass


















