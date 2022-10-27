<details open>
<summary><h1>generalpackager</h1></summary>

Tools to interface GitHub, PyPI, NPM and local modules / repos. Used for generating files to keep projects dry and synced. Tailored for my general packages.

<details>
<summary><h2>Table of Contents</h2></summary>

<pre>
<a href='#generalpackager'>generalpackager</a>
├─ <a href='#Dependency-Diagram-for-ManderaGeneral'>Dependency Diagram for ManderaGeneral</a>
├─ <a href='#Installation-showing-dependencies'>Installation showing dependencies</a>
├─ <a href='#Information'>Information</a>
├─ <a href='#Attributes'>Attributes</a>
├─ <a href='#Contributions'>Contributions</a>
└─ <a href='#Todo'>Todo</a>
</pre>
</details>


<details open>
<summary><h2>Dependency Diagram for ManderaGeneral</h2></summary>

```mermaid
flowchart LR
1([library]) --> 4([packager])
2([file]) --> 4([packager])
1([library]) --> 2([file])
0([import]) --> 1([library])
0([import]) --> 2([file])
1([library]) --> 3([vector])
click 0 "https://github.com/ManderaGeneral/generalimport"
click 1 "https://github.com/ManderaGeneral/generallibrary"
click 2 "https://github.com/ManderaGeneral/generalfile"
click 3 "https://github.com/ManderaGeneral/generalvector"
click 4 "https://github.com/ManderaGeneral/generalpackager"
style 4 fill:#482
```
</details>


<details open>
<summary><h2>Installation showing dependencies</h2></summary>

| `pip install`                                                                      | `generalpackager`   |
|:-----------------------------------------------------------------------------------|:--------------------|
| <a href='https://pypi.org/project/generallibrary[table]'>generallibrary[table]</a> | ✔️                  |
| <a href='https://pypi.org/project/generalfile'>generalfile</a>                     | ✔️                  |
| <a href='https://pypi.org/project/gitpython'>gitpython</a>                         | ✔️                  |
| <a href='https://pypi.org/project/pygithub'>pygithub</a>                           | ✔️                  |
| <a href='https://pypi.org/project/requests'>requests</a>                           | ✔️                  |
| <a href='https://pypi.org/project/pyinstaller'>pyinstaller</a>                     | ✔️                  |
| <a href='https://pypi.org/project/coverage'>coverage</a>                           | ✔️                  |
</details>


<details open>
<summary><h2>Information</h2></summary>

| Package                                                              | Ver                                                | Latest Release        | Python                                                                                                                                                                                                                                                 | Platform        | Cover   |
|:---------------------------------------------------------------------|:---------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|:--------|
| [generalpackager](https://github.com/ManderaGeneral/generalpackager) | [0.5.6](https://pypi.org/project/generalpackager/) | 2022-10-27 16:21 CEST | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/), [3.10](https://www.python.org/downloads/release/python-3100/), [3.11](https://www.python.org/downloads/release/python-3110/) | Windows, Ubuntu | 67.8 %  |
</details>



<details>
<summary><h2>Attributes</h2></summary>

<pre>
<a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/__init__.py#L1'>Module: generalpackager</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L12'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L12'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localmodule.py#L8'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L16'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager.py#L18'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L26'>Class: PyPI</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L28'>Method: api_url</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L44'>Method: download</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L40'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L96'>Method: get_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L64'>Method: get_owners_packages</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L83'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L71'>Method: get_website</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L33'>Property: git_clone_command</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L37'>Property: pip_install_command</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L108'>Method: request_kwargs</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L102'>Method: set_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L89'>Method: set_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L77'>Method: set_website</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L25'>Property: ssh_url</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L21'>Property: url</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localmodule.py#L8'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L12'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localmodule.py#L8'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L16'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager.py#L18'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L26'>Class: PyPI</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localmodule.py#L26'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localmodule.py#L67'>Method: get_all_local_modules</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localmodule.py#L89'>Method: get_dependants</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localmodule.py#L74'>Method: get_dependencies</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localmodule.py#L20'>Property: module</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localmodule.py#L41'>Property: objInfo</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/#L426'>Property: path</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L16'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L12'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localmodule.py#L8'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L16'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager.py#L18'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L26'>Class: PyPI</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/targets.py#L4'>Class: Targets</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_git.py#L28'>Method: commit</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_git.py#L34'>Property: commit_sha</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_git.py#L44'>Property: commit_sha_short</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L55'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L114'>Method: format_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_git.py#L9'>Method: get_commit_message</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L92'>Method: get_examples_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L60'>Method: get_exeproduct_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L56'>Method: get_exetarget_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L52'>Method: get_generate_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L16'>Method: get_git_exclude_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L64'>Method: get_git_ignore_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L72'>Method: get_index_js_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L44'>Method: get_init_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L28'>Method: get_license_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L24'>Method: get_manifest_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L12'>Method: get_metadata_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L68'>Method: get_npm_ignore_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L8'>Method: get_org_readme_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L80'>Method: get_package_json_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L72'>Method: get_package_paths_gen</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L84'>Method: get_pre_commit_hook_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L88'>Method: get_pre_push_hook_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L48'>Method: get_randomtesting_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L4'>Method: get_readme_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L20'>Method: get_setup_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L76'>Method: get_test_js_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L36'>Method: get_test_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L66'>Method: get_test_paths</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L40'>Method: get_test_template_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_paths.py#L32'>Method: get_workflow_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_git.py#L50'>Method: git_changed_files</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_git.py#L13'>Method: init_repo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_target.py#L18'>Method: is_django</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_target.py#L22'>Method: is_exe</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/name.py#L41'>Method: is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_target.py#L14'>Method: is_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_target.py#L10'>Method: is_python</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L33'>Property: metadata</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L48'>Method: metadata_exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/name.py#L37'>Method: name_is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_git.py#L19'>Property: repo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L60'>Method: repo_exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/name.py#L46'>Property: simple_name</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L42'>Property: target</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_target.py#L49'>Method: targetted</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/node/localrepo_node.py#L6'>Class: LocalRepo_Node</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/python/localrepo_python.py#L11'>Class: LocalRepo_Python</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/python/localrepo_python.py#L25'>Method: get_python_exe_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/python/localrepo_python.py#L16'>Method: get_venv_path</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/python/localrepo_python.py#L30'>Method: unittest</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager.py#L18'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L12'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localmodule.py#L8'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L16'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager.py#L18'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/other/packages.py#L9'>Class: Packages</a>
│  │  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/other/packages.py#L33'>Method: all_packages</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L26'>Class: PyPI</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/targets.py#L4'>Class: Targets</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_github.py#L37'>Method: commit_and_push</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/commit_editmsg.py#L5'>Class: commit_editmsg_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_files.py#L46'>Method: compare_local_to_github</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_files.py#L53'>Method: compare_local_to_pypi</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_files.py#L8'>Method: create_blank_locally_python</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_github.py#L57'>Method: create_github_repo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_github.py#L72'>Method: create_master_branch</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_github.py#L51'>Method: enable_vcs_operations</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/examples.py#L5'>Class: examples_folder</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/exeproduct.py#L5'>Class: exeproduct_folder</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/exetarget.py#L5'>Class: exetarget_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_relations.py#L65'>Method: general_bumped_set</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_relations.py#L73'>Method: general_changed_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/generate.py#L6'>Class: generate_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_files.py#L69'>Method: generate_localfiles</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_metadata.py#L27'>Method: get_classifiers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_relations.py#L26'>Method: get_dependants</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_relations.py#L7'>Method: get_dependencies</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/shared_files.py#L29'>Method: get_file_from_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/shared_files.py#L13'>Method: get_filenames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/shared_files.py#L19'>Method: get_files</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/shared_files.py#L24'>Method: get_files_by_relative_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_pypi.py#L8'>Method: get_latest_release</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_relations.py#L37'>Method: get_ordered_packagers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_relations.py#L59'>Method: get_owners_package_names</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_metadata.py#L4'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/git_exclude.py#L5'>Class: git_exclude_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_api.py#L81'>Property: github</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_api.py#L47'>Method: github_available</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_workflow.py#L53'>Method: if_publish_bump</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_workflow.py#L60'>Method: if_publish_upload</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/index_js.py#L6'>Class: index_js_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/init.py#L6'>Class: init_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_metadata.py#L33'>Method: is_bumped</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_target.py#L18'>Method: is_django</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_target.py#L22'>Method: is_exe</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/name.py#L41'>Method: is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_target.py#L14'>Method: is_node</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo_target.py#L10'>Method: is_python</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/license.py#L6'>Class: license_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_api.py#L88'>Property: localmodule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_api.py#L52'>Method: localmodule_available</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_api.py#L71'>Property: localrepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_api.py#L42'>Method: localrepo_available</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/manifest.py#L5'>Class: manifest_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/metadata.py#L5'>Class: metadata_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/name.py#L37'>Method: name_is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager.py#L57'>Method: new_clean_environment</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/npm_ignore.py#L5'>Class: npm_ignore_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/org_readme.py#L6'>Class: org_readme_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/package_json.py#L6'>Class: package_json_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager.py#L46'>Method: packagers_from_packages</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/pre_commit_hook.py#L4'>Class: pre_commit_hook_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/pre_push_hook.py#L6'>Class: pre_push_hook_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_github.py#L27'>Method: push</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_api.py#L95'>Property: pypi</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_api.py#L60'>Method: pypi_available</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/randomtesting.py#L6'>Class: randomtesting_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/readme.py#L9'>Class: readme_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_github.py#L21'>Property: remote</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_pypi.py#L23'>Method: reserve_name</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_workflow.py#L7'>Method: run_ordered_methods</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/setup.py#L6'>Class: setup_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/name.py#L46'>Property: simple_name</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager.py#L73'>Method: summary_packagers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_github.py#L11'>Method: sync_github_metadata</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_metadata.py#L47'>Property: target</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/test.py#L5'>Class: test_folder</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/test_js.py#L6'>Class: test_js_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/test_template.py#L6'>Class: test_template_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_workflow.py#L48'>Method: upload_package_summary</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/workflow.py#L6'>Class: workflow_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_workflow.py#L23'>Method: workflow_sync</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_workflow.py#L14'>Method: workflow_unittest</a>
└─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L26'>Class: PyPI</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L12'>Class: GitHub</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localmodule.py#L8'>Class: LocalModule</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L16'>Class: LocalRepo</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager.py#L18'>Class: Packager</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L26'>Class: PyPI</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L47'>Method: download</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L37'>Method: exists</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L70'>Method: get_date</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L59'>Method: get_owners_packages</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L41'>Method: get_tarball_url</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L63'>Method: get_version</a>
   └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L34'>Property: url</a>
</pre>
</details>


<details open>
<summary><h2>Contributions</h2></summary>

Issue-creation and discussions are most welcome!

Pull requests are not wanted, please discuss with me before investing any time
</details>


<details>
<summary><h2>Todo</h2></summary>

| Module                                                                                                                                                        | Message                                                                                                                                                                                                            |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/other/packages.py#L1'>packages.py</a>                                | <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/other/packages.py#L11'>Generate Python file in generalpackager containing general packages.</a>                           |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_github.py#L1'>packager_github.py</a>                        | <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_github.py#L41'>commit-hook failed for auto commit "not a valid Win32 application</a>                             |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_github.py#L1'>packager_github.py</a>                        | <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_github.py#L78'>Setup env vars for project.</a>                                                                   |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L1'>localrepo.py</a>                 | <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/base/localrepo.py#L21'>Search for imports to list dependencies.</a>                                         |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/python/metadata_python.py#L1'>metadata_python.py</a>   | <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/python/metadata_python.py#L4'>Dynamic values in DataClass to remove LocalRepos and Metadatas.</a>           |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/python/localrepo_python.py#L1'>localrepo_python.py</a> | <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/python/localrepo_python.py#L64'>Make sure twine is installed when trying to upload to pypi.</a>             |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/python/localrepo_python.py#L1'>localrepo_python.py</a> | <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/localrepo/python/localrepo_python.py#L65'>Look into private PyPI server where we could also do dry runs for test.</a> |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L1'>pypi.py</a>                                          | <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L12'>Move download to it's own package.</a>                                                                   |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L1'>pypi.py</a>                                          | <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/pypi.py#L66'>Find a faster fetch for latest PyPI version and datetime.</a>                                            |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/readme.py#L1'>readme.py</a>             | <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/shared/files/definitions/readme.py#L167'>Sort todos by name to decrease automatic commit changes.</a>                 |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L1'>github.py</a>                                      | <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/api/github.py#L14'>Get and Set GitHub repo private.</a>                                                                   |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_files.py#L1'>packager_files.py</a>                          | <a href='https://github.com/ManderaGeneral/generalpackager/blob/4df7d2cd/generalpackager/packager_files.py#L10'>Fix create_blank, it overwrites current projects pip install.</a>                                  |
</details>


<sup>
Generated 2022-10-27 16:21 CEST for commit <a href='https://github.com/ManderaGeneral/generalpackager/commit/4df7d2cd'>4df7d2cd</a>.
</sup>
</details>

