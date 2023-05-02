from generalpackager.api.shared.files.definitions.workflow import WorkflowFile


class WorkflowDevFile(WorkflowFile):
    _relative_path = ".github/workflows/workflow_dev.yml"


    def _generate(self):
        workflow = self.codeline()
        workflow.add_node(self._get_name())
        workflow.add_node(self._get_triggers(on_master=False))
        workflow.add_node(self._get_defaults())

        jobs = workflow.add_node("jobs:")
        jobs.add_node(self._get_unittest_job())
        jobs.add_node(self._get_sync_job())

        return workflow