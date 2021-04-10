# generalpackager
Tools to interface GitHub, PyPI and local modules / repos. Used for generating files to keep projects dry and synced. Tailored for my general packages.

This package and 3 other make up [ManderaGeneral](https://github.com/Mandera).

## Information
| Package                                                              | Ver                                              | Latest Release        | Python                                                                                                                   | Platform        |   Lvl | Todo                                                         | Tests   |
|:---------------------------------------------------------------------|:-------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|------:|:-------------------------------------------------------------|:--------|
| [generalpackager](https://github.com/ManderaGeneral/generalpackager) | [0.3](https://pypi.org/project/generalpackager/) | 2021-04-10 14:36 CEST | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu |     2 | [20](https://github.com/ManderaGeneral/generalpackager#Todo) | 86.2 %  |

## Contents
<pre>
<a href='#generalpackager'>generalpackager</a>
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
└─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L23'>Class: Packager</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L13'>Class: GitHub</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L31'>Method: download</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L27'>Method: exists</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L80'>Method: get_description</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L50'>Method: get_owners_packages</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L68'>Method: get_topics</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L58'>Method: get_website</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a> <b>(Untested)</b>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L86'>Method: set_description</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L74'>Method: set_topics</a>
   │  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L64'>Method: set_website</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L9'>Class: LocalModule</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L23'>Method: exists</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L64'>Method: get_all_local_modules</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L75'>Method: get_dependants</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L70'>Method: get_dependencies</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L55'>Method: get_env_vars</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a> <b>(Untested)</b>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L33'>Property: module</a>
   │  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L42'>Property: objInfo</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L22'>Class: LocalRepo</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L164'>Method: bump_version</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L177'>Method: create_sdist</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L193'>Property: description</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L193'>Property: enabled</a> <b>(Untested)</b>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L62'>Method: exists</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L193'>Property: extras_require</a> <b>(Untested)</b>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L130'>Method: get_git_exclude_path</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L133'>Method: get_license_path</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L132'>Method: get_manifest_path</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L129'>Method: get_metadata_path</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L151'>Method: get_package_paths_gen</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L95'>Method: get_path_from_name</a> <b>(Untested)</b>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L128'>Method: get_readme_path</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L82'>Method: get_repo_path_child</a> <b>(Untested)</b>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L74'>Method: get_repo_path_parent</a> <b>(Untested)</b>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L87'>Method: get_repos_path</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L131'>Method: get_setup_path</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L135'>Method: get_test_path</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L139'>Method: get_test_paths</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L134'>Method: get_workflow_path</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L159'>Method: git_changed_files</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L44'>Method: has_metadata</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L193'>Property: install_requires</a> <b>(Untested)</b>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a> <b>(Untested)</b>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L47'>Method: load_metadata</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L193'>Property: manifest</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L193'>Property: name</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L67'>Method: path_exists</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L168'>Method: pip_install</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L144'>Method: text_in_tests</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L193'>Property: topics</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L173'>Method: unittest</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L182'>Method: upload</a>
   │  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L193'>Property: version</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L25'>Class: PyPI</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L49'>Method: download</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L39'>Method: exists</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L70'>Method: get_date</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L61'>Method: get_owners_packages</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L43'>Method: get_tarball_url</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L65'>Method: get_version</a>
   │  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a> <b>(Untested)</b>
   │  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L75'>Method: reserve_name</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_github.py#L22'>Method: commit_and_push</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L82'>Method: compare_local_to_github</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L89'>Method: compare_local_to_pypi</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L54'>Method: exists</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L62'>Method: filter_relative_filenames</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L19'>Method: general_bumped_set</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L25'>Method: general_changed_dict</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L153'>Method: generate_git_exclude</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L159'>Method: generate_license</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L72'>Method: generate_localfiles</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L144'>Method: generate_manifest</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L219'>Method: generate_personal_readme</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L187'>Method: generate_readme</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L96'>Method: generate_setup</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L171'>Method: generate_workflow</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L176'>Method: get_attributes_markdown</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L10'>Method: get_badges_dict</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L26'>Method: get_classifiers</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L70'>Method: get_description_markdown</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L69'>Method: get_env</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L183'>Method: get_footnote_markdown</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L78'>Method: get_information_markdown</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L107'>Method: get_installation_markdown</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_pypi.py#L6'>Method: get_latest_release</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L6'>Method: get_ordered_packagers</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L13'>Method: get_owners_package_names</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L103'>Method: get_sync_job</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L63'>Method: get_todos</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L16'>Method: get_topics</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L22'>Method: get_triggers</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L89'>Method: get_unittest_job</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L33'>Method: get_untested_objInfo_dict</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L141'>Method: github_link</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L150'>Method: github_link_path_line</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L156'>Method: if_publish_bump</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L163'>Method: if_publish_publish</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L32'>Method: is_bumped</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L46'>Method: relative_path_is_aesthetic</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L119'>Method: run_ordered_methods</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L66'>Method: spawn_children</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L69'>Method: spawn_parents</a> <b>(Untested)</b>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L44'>Method: step_install_necessities</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L59'>Method: step_install_package_git</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L51'>Method: step_install_package_pip</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L112'>Method: step_run_packager_method</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L37'>Method: step_setup_python</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L80'>Method: steps_setup</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_github.py#L14'>Method: sync_github_metadata</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L134'>Method: workflow_sync</a>
   └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L126'>Method: workflow_unittest</a>
</pre>

## Todo
| Module                                                                                                                                     | Message                                                                                                                                                                                                  |
|:-------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>             | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L24'>Search for imports to list dependencies.</a>                                               |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L1'>pypi.py</a>                         | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L11'>Move download to it's own package.</a>                                                           |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L1'>pypi.py</a>                         | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L67'>Find a faster fetch for latest PyPI version.</a>                                                 |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L1'>pypi.py</a>                         | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L72'>Find a faster fetch for latest PyPI datetime.</a>                                                |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L1'>packager_files.py</a>         | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L30'>Watermark generated files to prevent mistake of thinking you can modify them directly.</a> |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L1'>packager.py</a>                     | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L4'>Add a check in workflow to make sure it doesn't use a pypi version in case of wrong order.</a>    |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L1'>packager.py</a>                     | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L26'>Allow github, pypi or local repo not to exist in any combination.</a>                            |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L1'>packager.py</a>                     | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L27'>Support writing [CI MAJOR] in msg to bump major for example.</a>                                 |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L1'>shared.py</a>                     | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Create unittest for 'is_general'.</a>                                                           |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>             | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L193'>Create unittest for 'enabled'.</a>                                                        |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>             | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L193'>Create unittest for 'extras_require'.</a>                                                 |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>             | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L95'>Create unittest for 'get_path_from_name'.</a>                                              |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>             | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L82'>Create unittest for 'get_repo_path_child'.</a>                                             |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>             | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L74'>Create unittest for 'get_repo_path_parent'.</a>                                            |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>             | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L193'>Create unittest for 'install_requires'.</a>                                               |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L1'>pypi.py</a>                         | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L75'>Create unittest for 'reserve_name'.</a>                                                          |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L1'>packager.py</a>                     | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L72'>Create unittest for 'generate_localfiles'.</a>                                                   |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L1'>packager_relations.py</a> | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L33'>Create unittest for 'get_untested_objInfo_dict'.</a>                                   |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L1'>packager.py</a>                     | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L66'>Create unittest for 'spawn_children'.</a>                                                        |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L1'>packager.py</a>                     | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L69'>Create unittest for 'spawn_parents'.</a>                                                         |

<sup>
Generated 2021-04-10 14:36 CEST for commit <a href='https://github.com/ManderaGeneral/generalpackager/commit/master'>master</a>.
</sup>
