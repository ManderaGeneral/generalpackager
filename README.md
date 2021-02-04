# generalpackager 0.0.13
Tools to interface GitHub, PyPI and local modules / repos. Used for generating files to keep projects dry and synced. Tailored for my general packages.

## Information
| name            |
|:----------------|
| generalpackager |

## Contents
<pre>
<a href='#generalpackager-0.0.13'>generalpackager 0.0.13</a>
├─ <a href='#Information'>Information</a>
├─ <a href='#Contents'>Contents</a>
├─ <a href='#Installation'>Installation</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Todo'>Todo</a>
</pre>

## Installation
| Command                       | <a href='https://pypi.org/project/pandas'>pandas</a>   | <a href='https://pypi.org/project/generallibrary'>generallibrary</a>   | <a href='https://pypi.org/project/generalfile'>generalfile</a>   | <a href='https://pypi.org/project/gitpython'>gitpython</a>   | <a href='https://pypi.org/project/requests'>requests</a>   |
|:------------------------------|:-------------------------------------------------------|:-----------------------------------------------------------------------|:-----------------------------------------------------------------|:-------------------------------------------------------------|:-----------------------------------------------------------|
| `pip install generalpackager` | Yes                                                    | Yes                                                                    | Yes                                                              | Yes                                                          | Yes                                                        |

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/__init__.py#L1'>Module: generalpackager</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L9'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L34'>Method: api_url</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L62'>Method: get_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L49'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L25'>Method: get_url</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L87'>Method: get_users_packages</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L38'>Method: get_website</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L20'>Method: is_creatable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L30'>Method: is_url_functioning</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L68'>Method: set_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L55'>Method: set_topics</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L44'>Method: set_website</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L8'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L43'>Method: get_all_packages</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L54'>Method: get_dependants</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L48'>Method: get_dependencies</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L34'>Method: get_env_vars</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L20'>Method: is_creatable</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L13'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L179'>Method: bump_version</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L155'>Method: commit_and_push</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L192'>Method: create_sdist</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L174'>Method: get_changed_files</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L88'>Method: get_git_exclude_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L100'>Method: get_license_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L116'>Method: get_local_repos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L96'>Method: get_manifest_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L84'>Method: get_metadata_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L112'>Method: get_package_paths</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L80'>Method: get_readme_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L53'>Method: get_repos_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L92'>Method: get_setup_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L108'>Method: get_test_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L135'>Method: get_todos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L104'>Method: get_workflow_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L66'>Method: is_creatable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L71'>Method: metadata_setter</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L124'>Method: path_is_repo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L183'>Method: pip_install</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L188'>Method: unittest</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L197'>Method: upload</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L16'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L9'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L8'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L13'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L27'>Class: PyPI</a>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L53'>Method: download_and_unpack_tarball</a>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L44'>Method: get_tarball_url</a>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L39'>Method: get_url</a>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L61'>Method: get_users_packages</a>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L69'>Method: get_version</a>
│  │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L34'>Method: is_creatable</a>
│  │  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L76'>Method: reserve_name</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L6'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_github.py#L19'>Method: clone_repo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_github.py#L31'>Method: commit_push_store_sha</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_pypi.py#L6'>Method: compare_local_to_pypi</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L75'>Method: compare_local_to_remote</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L62'>Method: configure_contents_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L55'>Method: filter_relative_filenames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L84'>Method: general_bumped_set</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L91'>Method: general_changed_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L139'>Method: generate_git_exclude</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L145'>Method: generate_license</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L87'>Method: generate_localfiles</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L130'>Method: generate_manifest</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L173'>Method: generate_readme</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L82'>Method: generate_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L157'>Method: generate_workflow</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L91'>Method: get_attributes_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L8'>Method: get_badges_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L26'>Method: get_classifiers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L57'>Method: get_dependencies</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L63'>Method: get_dependents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L71'>Method: get_env</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L98'>Method: get_footnote_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L20'>Method: get_information_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L37'>Method: get_installation_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L69'>Method: get_ordered_packagers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L31'>Method: get_packager_with_name</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L30'>Method: get_step</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L106'>Method: get_sync_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L16'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L22'>Method: get_triggers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L92'>Method: get_unittest_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L75'>Method: get_users_package_names</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L83'>Method: github_link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L156'>Method: if_publish_bump</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L161'>Method: if_publish_publish</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L32'>Method: is_bumped</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L46'>Method: is_creatable</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L45'>Method: load_general_packagers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L42'>Method: relative_path_is_aesthetic</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L15'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L122'>Method: run_ordered_methods</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L45'>Method: step_install_necessities</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L59'>Method: step_install_package_git</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L52'>Method: step_install_package_pip</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L115'>Method: step_run_packager_method</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L38'>Method: step_setup_python</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L82'>Method: steps_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_github.py#L11'>Method: sync_github_metadata</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L21'>Method: update_links</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L138'>Method: workflow_sync</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L130'>Method: workflow_unittest</a>
└─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L27'>Class: PyPI</a>
</pre>

## Todo
| Module               | Message                                                                                |
|:---------------------|:---------------------------------------------------------------------------------------|
| randomtesting.py     | Install packages in correct order when using git to prevent it using pip.              |
| randomtesting.py     | Write [CI MAJOR] in commit message to bump major for example.                          |
| randomtesting.py     | Push empty commits to dependents after publish in workflow.                            |
| randomtesting.py     | Generate GitHub profile readme.                                                        |
| randomtesting.py     | Compare local\_repo version with pypi version before publishing.                        |
| packager.py          | Allow github, pypi or local repo not to exist in any combination.                      |
| packager.py          | Replace badges with generated hardcode.                                                |
| packager.py          | Find all imports to generate install\_requires.                                         |
| packager.py          | Create links for Todos.                                                                |
| packager\_files.py    | Watermark generated files to prevent mistake of thinking you can modify them directly. |
| packager\_grp.py      | Maybe move PackagerGrp to Packager now that it inherits NetworkDiagram?                |
| packager\_markdown.py | Inherit future crawler class for pypi and github.                                      |
| pypi.py              | Move download to it's own package.                                                     |
| pypi.py              | Binary extension for generalfile.                                                      |
| pypi.py              | Add pack and unpack to generalfile.                                                    |

<sup>
Generated 2021-02-04 17:56 CET for commit <a href='https://github.com/ManderaGeneral/generalpackager/commit/master'>master</a>.
</sup>
