from typing import List

from generalfile import Path
from generallibrary import Terminal, Log, VerInfo, deco_require
from generalpackager.api.localrepo.base.localrepo import LocalRepo
from generalpackager.api.localrepo.node.metadata_node import Metadata_Node


class LocalRepo_Node(LocalRepo):
    _cls_target = LocalRepo.Targets.node
    _cls_metadata = Metadata_Node

    NPM_cmd = "npm.cmd" if VerInfo().windows else "npm"
    NODE_MODULES = "node_modules"

    @classmethod
    def _filt(cls, path):
        return (path / cls.NODE_MODULES).exists()

    def _node_modules_parent_path(self):
        contains_node_modules = self.path.get_parent(depth=-1, include_self=True, traverse_excluded=True, filt=self._filt)
        return contains_node_modules or self.path

    def package_folder(self, local=True):
        if local:
            return self._node_modules_parent_path() / self.NODE_MODULES
        npm_root = Terminal(self.NPM_cmd, "root", "-g").string_result
        return Path(path=npm_root)

    def run_tests(self):
        with self.path.as_working_dir():
            Terminal("jest", capture_output=False)

    UNINSTALL = "uninstall"

    def _stall(self, local, editable, normal_cmd, editable_cmd):
        cmd = editable_cmd if editable else normal_cmd
        name = self.name if normal_cmd == self.UNINSTALL else self.path.absolute()
        args = [self.NPM_cmd, cmd, G := "-g", name]
        if local:
            args.remove(G)

        Log(__name__).debug(args)

        package_folder = self.package_folder(local=local)
        with package_folder.as_working_dir():
            Terminal(*args, capture_output=False)

    @deco_require(LocalRepo.exists)
    def install(self, local=True, editable=False):
        self._stall(local=local, editable=editable, normal_cmd="install", editable_cmd="link")

    @deco_require(LocalRepo.exists)
    def uninstall(self, local=True, editable=False):
        self._stall(local=local, editable=editable, normal_cmd=self.UNINSTALL, editable_cmd="unlink")

    @deco_require(LocalRepo.exists)
    def publish(self, public=True):
        Log(__name__).debug(f"Publish for {self.name}")

        with self.path.as_working_dir():
            Terminal(self.NPM_cmd, "publish", capture_output=False)

    def list_packages(self, local=True, editable=None) -> List[str]:
        args = [self.NPM_cmd, "list", "-g"]
        if local:
            args.remove("-g")

        package_folder = self.package_folder(local=local)
        with package_folder.as_working_dir():
            terminal = Terminal(*args, error=False)

        if terminal.fail:
            return

        for line in terminal.string_result.splitlines():
            if "-- " in line and "@" in line:
                base, *link = line.split(" -> ")
                if editable is None or editable is bool(link):
                    name, version = base.split()[1].split("@")
                    yield name

















