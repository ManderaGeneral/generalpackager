
from generalpackager.api.shared.files.file import File


class WorkflowFile(File):
    _relative_path = ".github/workflows/workflow.yml"
    aesthetic = True

    def generate(self):
        pass

