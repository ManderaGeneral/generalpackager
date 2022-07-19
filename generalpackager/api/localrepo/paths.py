

class _LocalRepo_Paths:
    def get_readme_path(self):              return self.path / "README.md"
    def get_org_readme_path(self):          return self.path / "profile/README.md"
    def get_metadata_path(self):            return self.path / "metadata.json"
    def get_git_exclude_path(self):         return self.path / ".git/info/exclude"
    def get_setup_path(self):               return self.path / "setup.py"
    def get_manifest_path(self):            return self.path / "MANIFEST.in"
    def get_license_path(self):             return self.path / "LICENSE"
    def get_workflow_path(self):            return self.path / ".github/workflows/workflow.yml"
    def get_test_path(self):                return self.path / f"{self.metadata.name}/test"
    def get_test_template_path(self):       return self.get_test_path() / f"test_{self.metadata.name}.py"
    def get_init_path(self):                return self.path / self.metadata.name / "__init__.py"
    def get_randomtesting_path(self):       return self.path / "randomtesting.py"
    def get_generate_path(self):            return self.path / "generate.py"
    def get_exetarget_path(self):           return self.path / "exetarget.py"
    def get_exeproduct_path(self):          return self.path / "dist/exetarget"
    def get_git_ignore_path(self):          return self.path / ".gitignore"

    def get_npm_ignore_path(self):          return self.path / ".npmignore"
    def get_index_js_path(self):            return self.path / "index.js"
    def get_test_js_path(self):             return self.path / "test.js"
    def get_package_json_path(self):        return self.path / "package.json"

