# generalpackager
Tools to interface GitHub, PyPI and local modules / repos. Used for generating files to keep projects dry and synced. Tailored for my general packages.

This package and 5 other make up [ManderaGeneral](https://github.com/ManderaGeneral).

## Information
| Package                                                              | Ver                                                | Latest Release       | Python                                                                                                                   | Platform        |   Lvl | Todo                                                         | Tests   |
|:---------------------------------------------------------------------|:---------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|------:|:-------------------------------------------------------------|:--------|
| [generalpackager](https://github.com/ManderaGeneral/generalpackager) | [0.3.8](https://pypi.org/project/generalpackager/) | 2021-11-19 00:35 CET | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu |     2 | [19](https://github.com/ManderaGeneral/generalpackager#Todo) | 91.8 %  |

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
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L13'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L32'>Method: download</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L28'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L84'>Method: get_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L54'>Method: get_owners_packages</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L72'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L62'>Method: get_website</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L90'>Method: set_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L78'>Method: set_topics</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L68'>Method: set_website</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L9'>Class: LocalModule</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L23'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L63'>Method: get_all_local_modules</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L81'>Method: get_dependants</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L69'>Method: get_dependencies</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L54'>Method: get_env_vars</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L29'>Property: module</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L38'>Property: objInfo</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L21'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L182'>Method: bump_version</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L200'>Method: create_sdist</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L226'>Property: description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L226'>Property: enabled</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L74'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L226'>Property: extras_require</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L215'>Method: generate_exe</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L146'>Method: get_git_exclude_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L153'>Method: get_init_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L149'>Method: get_license_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L148'>Method: get_manifest_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L66'>Method: get_metadata_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L145'>Method: get_metadata_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L144'>Method: get_org_readme_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L169'>Method: get_package_paths_gen</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L107'>Method: get_path_from_name</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L154'>Method: get_randomtesting_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L143'>Method: get_readme_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L94'>Method: get_repo_path_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L86'>Method: get_repo_path_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L99'>Method: get_repos_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L147'>Method: get_setup_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L151'>Method: get_test_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L157'>Method: get_test_paths</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L152'>Method: get_test_template_path</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L150'>Method: get_workflow_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L177'>Method: git_changed_files</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L46'>Method: has_metadata</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L226'>Property: install_requires</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L226'>Property: installable</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L49'>Method: load_metadata</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L226'>Property: manifest</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L226'>Property: name</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L79'>Method: path_exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L186'>Method: pip_install</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L192'>Method: pip_uninstall</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L226'>Property: private</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L162'>Method: text_in_tests</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L226'>Property: topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L196'>Method: unittest</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L205'>Method: upload</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L226'>Property: version</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L70'>Method: write_metadata</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L23'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_github.py#L20'>Method: commit_and_push</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L114'>Method: compare_local_to_github</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L121'>Method: compare_local_to_pypi</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L64'>Method: create_blank_locally</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L63'>Method: exists</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L93'>Method: filter_relative_filenames</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L36'>Method: general_bumped_set</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L42'>Method: general_changed_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L188'>Method: generate_git_exclude</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L194'>Method: generate_license</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L294'>Method: generate_localfiles</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L179'>Method: generate_manifest</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L252'>Method: generate_personal_readme</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L276'>Method: generate_randomtesting</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L222'>Method: generate_readme</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L128'>Method: generate_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L284'>Method: generate_test_template</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L206'>Method: generate_workflow</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L203'>Method: get_attributes_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L10'>Method: get_badges_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L26'>Method: get_classifiers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L15'>Method: get_dependants</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L6'>Method: get_dependencies</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L84'>Method: get_description_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L81'>Method: get_env</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L209'>Method: get_footnote_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L90'>Method: get_information_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L119'>Method: get_installation_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_pypi.py#L6'>Method: get_latest_release</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L55'>Method: get_new_packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L23'>Method: get_ordered_packagers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L30'>Method: get_owners_package_names</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L116'>Method: get_sync_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L63'>Method: get_todos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L70'>Method: get_todos_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L16'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L23'>Method: get_triggers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L102'>Method: get_unittest_job</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_relations.py#L50'>Method: get_untested_objInfo_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L153'>Method: github_link</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L162'>Method: github_link_path_line</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L175'>Method: if_publish_bump</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L182'>Method: if_publish_publish</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L32'>Method: is_bumped</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L77'>Method: relative_path_is_aesthetic</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L132'>Method: run_ordered_methods</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L51'>Method: spawn_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L57'>Method: spawn_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L51'>Method: step_install_necessities</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L66'>Method: step_install_package_git</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L58'>Method: step_install_package_pip</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L125'>Method: step_run_packager_method</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L44'>Method: step_setup_python</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L38'>Method: step_setup_ssh</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L92'>Method: steps_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_github.py#L12'>Method: sync_github_metadata</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L168'>Method: upload_package_summary</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L147'>Method: workflow_sync</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L139'>Method: workflow_unittest</a>
└─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L25'>Class: PyPI</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L49'>Method: download</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L39'>Method: exists</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L71'>Method: get_date</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L61'>Method: get_owners_packages</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L43'>Method: get_tarball_url</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L66'>Method: get_version</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/shared.py#L4'>Method: is_general</a>
   └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L76'>Method: reserve_name</a>
</pre>

## Todo
| Module                                                                                                                                   | Message                                                                                                                                                                                                  |
|:-----------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L1'>packager.py</a>                   | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L4'>Prevent workflow using pypi to install a general package.</a>                                     |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>           | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L23'>Search for imports to list dependencies.</a>                                               |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>           | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L139'>Decoupled JSON serialize instructions with custom dumps in lib.</a>                       |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>           | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L207'>Make sure twine is installed when trying to upload to pypi.</a>                           |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L1'>pypi.py</a>                       | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L11'>Move download to it's own package.</a>                                                           |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L1'>pypi.py</a>                       | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L65'>Find a faster fetch for latest PyPI version and datetime.</a>                                    |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L1'>github.py</a>                   | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L15'>Get and Set GitHub repo private.</a>                                                           |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L1'>packager_files.py</a>       | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L33'>Watermark generated files to prevent mistake of thinking you can modify them directly.</a> |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>           | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L215'>[UnitTest] for Method: generate_exe</a>                                                   |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>           | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L144'>[UnitTest] for Method: get_org_readme_path</a>                                            |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>           | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L154'>[UnitTest] for Method: get_randomtesting_path</a>                                         |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>           | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L152'>[UnitTest] for Method: get_test_template_path</a>                                         |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>           | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L226'>[UnitTest] for Property: installable</a>                                                  |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L1'>local_repo.py</a>           | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L226'>[UnitTest] for Property: private</a>                                                      |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L1'>packager_files.py</a>       | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L64'>[UnitTest] for Method: create_blank_locally</a>                                            |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L1'>packager_files.py</a>       | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L276'>[UnitTest] for Method: generate_randomtesting</a>                                         |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L1'>packager_files.py</a>       | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L284'>[UnitTest] for Method: generate_test_template</a>                                         |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L1'>packager_workflow.py</a> | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L38'>[UnitTest] for Method: step_setup_ssh</a>                                               |
| <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L1'>packager_workflow.py</a> | <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_workflow.py#L168'>[UnitTest] for Method: upload_package_summary</a>                                      |

<sup>
Generated 2021-11-19 18:14 CET for commit <a href='https://github.com/ManderaGeneral/generalpackager/commit/master'>master</a>.
</sup>
