from generallibrary import Markdown

from generalpackager.api.shared.files.file import File


class OrgReadmeFile(File):
    @property
    def _relative_path(self):
        if self.packager.name == ".github":
            return "profile/README.md"
        else:
            return self.packager.readme_file.relative_path

    aesthetic = True

    @staticmethod
    def get_org_description_markdown():
        return Markdown(header="ManderaGeneral").add_list_lines(
            "Modularized platform for managing future products.",
            "Automatic workflows to unittest, sync and publish.",
        )

    def generate(self):
        ordered_packagers = self.packager.get_ordered_packagers(include_private=False)

        # Description
        markdown = self.get_org_description_markdown()

        # Mermaid
        self.packager.get_mermaid_markdown().set_parent(parent=markdown)

        # Package information
        self.packager.get_information_markdown(*ordered_packagers).set_parent(parent=markdown)

        # Contributions
        self.packager.get_contributions_markdown().set_parent(parent=markdown)

        # Generation timestamp
        self.packager.get_footnote_markdown(commit=False).set_parent(parent=markdown)

        return markdown

