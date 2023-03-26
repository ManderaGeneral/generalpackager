from generalfile import Path
from generallibrary import join_with_str, clipboard_copy
from generalpackager.api.shared.files.file_fetcher import FileFetcher


class _Files_Helpers:
    def _get_files_as_tsv(self):
        """ :param generalpackager.Packager or generalpackager.LocalRepo self: """
        columns = {
            "name": lambda x: type(x).__name__,
            "path": lambda x: x._relative_path,
            "generatable": lambda x: x.has_generate_instructions(),
            "aesthetic": lambda x: x.aesthetic,
            "remove": lambda x: x.remove,
            "overwrite": lambda x: x.overwrite,
            "is_file": lambda x: x.is_file,
            "target": lambda x: x.target,
        }

        lines = ["\t".join(columns)]
        for file in self.get_files():
            lines.append(join_with_str("\t", [func(file) for func in columns.values()]))

        csv = "\n".join(lines)
        print(clipboard_copy(csv))

    @staticmethod
    def _get_file_fetcher_definitions():
        lines = ["# Generated with Packager._get_file_fetcher_definitions()"]
        definitions = Path("./definitions").get_children()
        definitions = sorted(definitions, key=lambda path: path.name())
        for definition in definitions:
            stem = definition.stem()
            if stem.startswith("_"):
                continue

            filefetcher = FileFetcher()
            filefetcher.name = stem
            file = filefetcher.cls

            suffix = "file" if file.is_file else "folder"
            lines.append(f"{stem}_{suffix} = FileFetcher()")
        result = "\n".join([f"    {line}" for line in lines])
        print(clipboard_copy(result))

if __name__ == "__main__":
    from generalpackager import Packager
    Packager._get_file_fetcher_definitions()


