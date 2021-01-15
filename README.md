# generalpackager
Tools to interface GitHub, PyPI and local modules / repos. Used for generating files to keep projects dry and synced.

[![workflow Actions Status](https://github.com/ManderaGeneral/generalpackager/workflows/workflow/badge.svg)](https://github.com/ManderaGeneral/generalpackager/actions)
![GitHub last commit](https://img.shields.io/github/last-commit/ManderaGeneral/generalpackager)
[![PyPI version shields.io](https://img.shields.io/pypi/v/generalpackager.svg)](https://pypi.org/project/generalpackager/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/generalpackager.svg)](https://pypi.python.org/pypi/generalpackager/)
[![Generic badge](https://img.shields.io/badge/platforms-windows%20%7C%20ubuntu-blue.svg)](https://shields.io/)

## Contents
<pre>
<a href='#generalpackager'>generalpackager</a>
├─ <a href='#Contents'>Contents</a>
├─ <a href='#Installation'>Installation</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Todos'>Todos</a>
</pre>

## Installation
| Command                       | <a href='https://pypi.org/project/pandas'>pandas</a>   | <a href='https://pypi.org/project/generallibrary'>generallibrary</a>   | <a href='https://pypi.org/project/generalfile'>generalfile</a>   | <a href='https://pypi.org/project/gitpython'>gitpython</a>   | <a href='https://pypi.org/project/requests'>requests</a>   |
|:------------------------------|:-------------------------------------------------------|:-----------------------------------------------------------------------|:-----------------------------------------------------------------|:-------------------------------------------------------------|:-----------------------------------------------------------|
| `pip install generalpackager` | Yes                                                    | Yes                                                                    | Yes                                                              | Yes                                                          | Yes                                                        |

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/__init__.py#L1'>Module: generalpackager</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/github.py#L7'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/github.py#L25'>Method: api_url</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/github.py#L15'>Method: assert_url_up</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/github.py#L53'>Method: get_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/github.py#L40'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/github.py#L29'>Method: get_website</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/github.py#L59'>Method: set_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/github.py#L46'>Method: set_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/github.py#L35'>Method: set_website</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/github.py#L21'>Method: url</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_module.py#L7'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_module.py#L31'>Method: get_all_packages</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_module.py#L42'>Method: get_dependants</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_module.py#L36'>Method: get_dependencies</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_module.py#L22'>Method: get_env_vars</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L10'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L134'>Method: bump_version</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L122'>Method: commit_and_push</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L62'>Method: get_git_exclude_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L70'>Method: get_license_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L86'>Method: get_local_repos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L58'>Method: get_metadata_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L82'>Method: get_package_paths</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L54'>Method: get_readme_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L66'>Method: get_setup_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L78'>Method: get_test_main_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L102'>Method: get_todos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L74'>Method: get_workflow_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L45'>Method: metadata_setter</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/local_repo.py#L91'>Method: path_is_repo</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager.py#L18'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_markdown.py#L46'>Method: configure_contents_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_pypi.py#L6'>Method: create_sdist</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_files.py#L8'>Method: generate_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_files.py#L63'>Method: generate_git_exclude</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_files.py#L69'>Method: generate_license</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager.py#L52'>Method: generate_localfiles</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_markdown.py#L90'>Method: generate_readme</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_files.py#L16'>Method: generate_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_files.py#L81'>Method: generate_workflow</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_markdown.py#L75'>Method: get_attributes_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_markdown.py#L8'>Method: get_badges_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_metadata.py#L26'>Method: get_classifiers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L74'>Method: get_env</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_markdown.py#L82'>Method: get_footnote_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_markdown.py#L21'>Method: get_installation_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L30'>Method: get_step</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L119'>Method: get_sync_and_publish_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_metadata.py#L16'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L22'>Method: get_triggers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L99'>Method: get_unittest_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_markdown.py#L67'>Method: github_link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L37'>Method: step_checkout</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L51'>Method: step_install_necessities</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L66'>Method: step_install_package_git</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L58'>Method: step_install_package_pip</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L94'>Method: step_publish</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L44'>Method: step_setup_python</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L87'>Method: step_sync</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_workflow.py#L82'>Method: step_unittests</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_github.py#L5'>Method: sync_github_metadata</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager.py#L60'>Method: sync_package</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/packager_pypi.py#L14'>Method: upload</a>
└─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/pypi.py#L6'>Class: PyPI</a>
   └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/53d41952a0055ffd63d74227e44aee23986e4511/generalpackager/api/pypi.py#L13'>Method: get_users_packages</a>
</pre>

## Todos
| Module               | Message                                                                       |
|:---------------------|:------------------------------------------------------------------------------|
| randomtesting.py     | Write [CI MAJOR] in commit message to bump major for example.                 |
| randomtesting.py     | Push empty commits to dependents after publish in workflow.                   |
| randomtesting.py     | Generate GitHub profile readme.                                               |
| randomtesting.py     | Compare local\_repo version with pypi version before publishing.               |
| packager\_workflow.py | Add token here to see if we can trigger workflow for dependents auto testing. |
| packager.py          | Allow github, pypi or local repo not to exist in any combination.             |
| packager\_markdown.py | Inherit future crawler class for pypi and github.                             |

<sup>
Generated 2021-01-15 12:48 CET for commit <a href='https://github.com/ManderaGeneral/generalpackager/commit/53d41952a0055ffd63d74227e44aee23986e4511'>53d41952a0055ffd63d74227e44aee23986e4511</a>.
</sup>
