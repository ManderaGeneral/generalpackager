# generalpackager
Tools to interface GitHub, PyPI and local modules / repos. Used for generating files to keep projects dry and synced.

[![workflow Actions Status](https://github.com/ManderaGeneral/generalpackager/workflows/workflow/badge.svg)](https://github.com/ManderaGeneral/generalpackager/actions)
![GitHub last commit](https://img.shields.io/github/last-commit/ManderaGeneral/generalpackager)
[![PyPI version shields.io](https://img.shields.io/pypi/v/generalpackager.svg)](https://pypi.org/project/generalpackager/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/generalpackager.svg)](https://pypi.python.org/pypi/generalpackager/)
[![Generic badge](https://img.shields.io/badge/platforms-Windows%20%7C%20Ubuntu%20%7C%20MacOS-blue.svg)](https://shields.io/)

## Contents
<pre>
<a href='#generalpackager'>generalpackager</a>
├─ <a href='#Contents'>Contents</a>
├─ <a href='#Installation'>Installation</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Todos'>Todos</a>
</pre>

## Installation
```
pip install generalpackager
```

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/__init__.py#L1'>Module: generalpackager</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L7'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L25'>Method: api_url</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L15'>Method: assert_url_up</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L53'>Method: get_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L40'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L29'>Method: get_website</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L59'>Method: set_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L46'>Method: set_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L35'>Method: set_website</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L21'>Method: url</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L5'>Class: LocalModule</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L20'>Method: get_env_vars</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L10'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L127'>Method: bump_version</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L115'>Method: commit_and_push</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L55'>Method: get_git_exclude_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L63'>Method: get_license_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L79'>Method: get_local_repos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L51'>Method: get_metadata_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L75'>Method: get_package_paths</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L47'>Method: get_readme_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L59'>Method: get_setup_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L71'>Method: get_test_main_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L95'>Method: get_todos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L67'>Method: get_workflow_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L38'>Method: metadata_setter</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L84'>Method: path_is_repo</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L18'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L39'>Method: configure_contents_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_pypi.py#L6'>Method: create_sdist</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L8'>Method: generate_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L58'>Method: generate_git_exclude</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L64'>Method: generate_license</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L53'>Method: generate_localfiles</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L83'>Method: generate_readme</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L16'>Method: generate_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L76'>Method: generate_workflow</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L68'>Method: get_attributes_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L9'>Method: get_badges_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L26'>Method: get_classifiers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L61'>Method: get_env</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L75'>Method: get_footnote_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L22'>Method: get_installation_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L35'>Method: get_step</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L81'>Method: get_sync_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L16'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L27'>Method: get_triggers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L95'>Method: get_unittest_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L60'>Method: github_link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L42'>Method: step_checkout</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L53'>Method: step_install_package</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L69'>Method: step_run_unittests</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L46'>Method: step_setup_python</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L74'>Method: step_sync</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_github.py#L5'>Method: sync_github_metadata</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L61'>Method: sync_package</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_pypi.py#L14'>Method: upload</a>
└─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L3'>Class: PyPI</a>
</pre>

## Todos
| Module               | Message                                                           |
|:---------------------|:------------------------------------------------------------------|
| randomtesting.py     | Automatically insert empty line when indent retracts              |
| randomtesting.py     | Write [CI MAJOR] in commit message to bump major for example      |
| randomtesting.py     | Remove test/main.py                                               |
| packager_markdown.py | Inherit future crawler class for pypi and github.                 |
| packager_markdown.py | Use Packager.os for badges.                                       |
| packager.py          | Allow github, pypi or local repo not to exist in any combination. |
| pypi.py              | Method to upload to PyPI.                                         |

<sup>
Generated 2021-01-14 08:33 CET for commit <a href='https://github.com/ManderaGeneral/generalpackager/commit/master'>master</a>.
</sup>