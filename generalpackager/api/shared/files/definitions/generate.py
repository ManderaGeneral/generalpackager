from generallibrary import CodeLine

from generalpackager.api.shared.files.file import File


class GenerateFile(File):
    _relative_path = "generate.py"
    aesthetic = True

    def _generate(self):
        """ Generate randomtesting.py. """
        top = CodeLine()
        top.add_node(CodeLine(f"from generalpackager import Packager", space_before=1, space_after=1))
        main = top.add_node(CodeLine(f'if __name__ == "__main__":'))
        main.add_node(CodeLine(f"""Packager("{self.packager.name}").generate_localfiles(print_out=True)""", space_after=50))
        return top

