

class _PackagerPackageType:
    supported_package_types = "Python", "Node"

    def __init_post__(self, package_type):
        self._package_type_check(package_type)

    def _package_type_check(self, package_type):
        if package_type not in (None, ) + self.supported_package_types:
            raise AssertionError(f"package_type must be None or {' or '.join(self.supported_package_types)}")
        if package_type is not None and self.localrepo.package_type is not None and package_type is not self.localrepo.package_type:
            raise AssertionError(f"package_type was set to '{package_type}' but '{self.name}' is already a '{self.localrepo.package_type}' package")
