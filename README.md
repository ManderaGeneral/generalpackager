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
<a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/__init__.py#L1'>Module: generalpackager</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L9'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L34'>Method: api_url</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L62'>Method: get_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L49'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L25'>Method: get_url</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L87'>Method: get_users_packages</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L38'>Method: get_website</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L20'>Method: is_creatable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L30'>Method: is_url_functioning</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L68'>Method: set_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L55'>Method: set_topics</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L44'>Method: set_website</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_module.py#L8'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_module.py#L43'>Method: get_all_packages</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_module.py#L54'>Method: get_dependants</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_module.py#L48'>Method: get_dependencies</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_module.py#L34'>Method: get_env_vars</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_module.py#L20'>Method: is_creatable</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L13'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L162'>Method: bump_version</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L145'>Method: commit_and_push</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L177'>Method: create_sdist</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L157'>Method: get_changed_files</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L82'>Method: get_git_exclude_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L90'>Method: get_license_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L106'>Method: get_local_repos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L78'>Method: get_metadata_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L102'>Method: get_package_paths</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L74'>Method: get_readme_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L47'>Method: get_repos_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L86'>Method: get_setup_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L98'>Method: get_test_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L125'>Method: get_todos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L94'>Method: get_workflow_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L60'>Method: is_creatable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L65'>Method: metadata_setter</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L114'>Method: path_is_repo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L166'>Method: pip_install</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L172'>Method: unittest</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L185'>Method: upload</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager.py#L16'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/github.py#L9'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_module.py#L8'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/local_repo.py#L13'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/pypi.py#L8'>Class: PyPI</a>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/pypi.py#L21'>Method: get_url</a>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/pypi.py#L26'>Method: get_users_packages</a>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/pypi.py#L33'>Method: get_version</a>
│  │  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/pypi.py#L16'>Method: is_creatable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_relations.py#L6'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_github.py#L16'>Method: clone_repo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_markdown.py#L46'>Method: configure_contents_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_files.py#L94'>Method: generate_git_exclude</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_files.py#L100'>Method: generate_license</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager.py#L89'>Method: generate_localfiles</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_files.py#L128'>Method: generate_readme</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_files.py#L47'>Method: generate_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_files.py#L112'>Method: generate_workflow</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_markdown.py#L75'>Method: get_attributes_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_markdown.py#L8'>Method: get_badges_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_files.py#L35'>Method: get_changed_files</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_metadata.py#L26'>Method: get_classifiers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_relations.py#L56'>Method: get_dependencies</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_relations.py#L62'>Method: get_dependents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L75'>Method: get_env</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_markdown.py#L82'>Method: get_footnote_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_markdown.py#L21'>Method: get_installation_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_relations.py#L68'>Method: get_ordered_packagers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_relations.py#L31'>Method: get_packager_with_name</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L30'>Method: get_step</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L130'>Method: get_sync_push_publish_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_metadata.py#L16'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L22'>Method: get_triggers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L101'>Method: get_unittest_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_relations.py#L74'>Method: get_users_package_names</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_markdown.py#L67'>Method: github_link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_metadata.py#L32'>Method: is_bumped</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager.py#L48'>Method: is_creatable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_relations.py#L45'>Method: load_general_packagers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_relations.py#L15'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L38'>Method: step_checkout</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L148'>Method: step_grp_clone</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L52'>Method: step_install_necessities</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L66'>Method: step_install_package_git</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L59'>Method: step_install_package_pip</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L96'>Method: step_publish</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L45'>Method: step_setup_python</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L90'>Method: step_sync</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L85'>Method: step_unittests</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_github.py#L8'>Method: sync_github_metadata</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager.py#L95'>Method: sync_package</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_relations.py#L21'>Method: update_links</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_workflow.py#L155'>Method: workflow_stuff</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_grp.py#L13'>Class: PackagerGrp</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_grp.py#L27'>Method: add_packages_from_names</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_grp.py#L31'>Method: clone</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_grp.py#L41'>Method: get_bumped</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_grp.py#L36'>Method: install</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/packager_grp.py#L23'>Method: load_general_packages</a>
└─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/6c7dd3ca1e5eb1e618167b802c89216d93798623/generalpackager/api/pypi.py#L8'>Class: PyPI</a>
</pre>

## Todos
| Module               | Message                                                                       |
|:---------------------|:------------------------------------------------------------------------------|
| randomtesting.py     | Install packages in correct order when using git to prevent it using pip.     |
| randomtesting.py     | Write [CI MAJOR] in commit message to bump major for example.                 |
| randomtesting.py     | Push empty commits to dependents after publish in workflow.                   |
| randomtesting.py     | Generate GitHub profile readme.                                               |
| randomtesting.py     | Compare local\_repo version with pypi version before publishing.               |
| packager\_workflow.py | Add token here to see if we can trigger workflow for dependents auto testing. |
| packager\_markdown.py | Inherit future crawler class for pypi and github.                             |
| packager\_grp.py      | Maybe move PackagerGrp to Packager now that it inherits NetworkDiagram?       |
| packager.py          | Allow github, pypi or local repo not to exist in any combination.             |
| packager.py          | Replace badges with generated hardcode.                                       |
| pypi.py              | get\_latest\_version()                                                          |

<sup>
Generated 2021-01-29 11:42 CET for commit <a href='https://github.com/ManderaGeneral/generalpackager/commit/6c7dd3ca1e5eb1e618167b802c89216d93798623'>6c7dd3ca1e5eb1e618167b802c89216d93798623</a>.
</sup>
