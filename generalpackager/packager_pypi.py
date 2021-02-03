
from generalfile import Path

from pprint import pprint


class _PackagerPypi:
    def compare_local_to_pypi(self):
        """ :param generalpackager.Packager self: """
        target = Path.get_cache_dir() / "Python"
        self.pypi.download_and_unpack_tarball(target_folder=target)

        target /= f"{self.name}-{self.pypi.get_version()}"

        def _filter(path):
            """ :param Path path: """
            return not any([part in self.git_exclude_lines for part in path.parts()])

        pprint(self.path.get_differing_files(target=target, filt=_filter))



