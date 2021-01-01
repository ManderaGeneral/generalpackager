# generalpackager
Tools to interface GitHub, PyPI and local modules / repos. Used for generating files to keep projects dry and synced.

| UnitTests                                                                                                                                                               | Alerts                                                                                                                                                                                | Commit                                                                                          | Release                                                                                                                    | Python                                                                                                                          | Operating System                                                                                                              |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [![workflow Actions Status](https://github.com/ManderaGeneral/generalpackager/workflows/workflow/badge.svg)](https://github.com/ManderaGeneral/generalpackager/actions) | [![Total alerts](https://img.shields.io/lgtm/alerts/g/ManderaGeneral/generalpackager.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ManderaGeneral/generalpackager/alerts/) | ![GitHub last commit](https://img.shields.io/github/last-commit/ManderaGeneral/generalpackager) | [![PyPI version shields.io](https://img.shields.io/pypi/v/generalpackager.svg)](https://pypi.org/project/generalpackager/) | [![PyPI pyversions](https://img.shields.io/pypi/pyversions/generalpackager.svg)](https://pypi.python.org/pypi/generalpackager/) | [![Generic badge](https://img.shields.io/badge/platforms-Windows%20%7C%20Ubuntu%20%7C%20MacOS-blue.svg)](https://shields.io/) |

## Contents
<pre>
<a href='#generalpackager'>generalpackager</a>
├─ <a href='#Contents'>Contents</a>
├─ <a href='#Installation'>Installation</a>
│  └─ <a href='#Extras'>Extras</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Todos'>Todos</a>
</pre>

## Installation
```
pip install generalpackager
```

### Extras
| Name    | Command                                | Extra packages             |
|:--------|:---------------------------------------|:---------------------------|
| testing | `pip install generalpackager[testing]` | `hello`, `there` and `foo` |
| another | `pip install generalpackager[another]` | `omg` and `hello`          |

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/__init__.py#L1'>Module: generalpackager</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L7'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L20'>Method: api_url</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L48'>Method: get_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L35'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L24'>Method: get_website</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L54'>Method: set_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L41'>Method: set_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L30'>Method: set_website</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L16'>Method: url</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L5'>Class: LocalModule</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L9'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L73'>Method: commit_and_push</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L25'>Method: get_git_exclude_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L37'>Method: get_local_repos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L21'>Method: get_metadata_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L33'>Method: get_package_paths</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L17'>Method: get_readme_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L29'>Method: get_setup_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L53'>Method: get_todos</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L42'>Method: path_is_repo</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L18'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L39'>Method: configure_contents_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L7'>Method: generate_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L52'>Method: generate_git_exclude</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L67'>Method: generate_readme</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files.py#L15'>Method: generate_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L60'>Method: get_attributes_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L8'>Method: get_badges_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L26'>Method: get_classifiers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown.py#L22'>Method: get_installation_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata.py#L16'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L48'>Method: setup_all</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_github.py#L5'>Method: sync_github_metadata</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L3'>Class: PyPI</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/__init__.py#L10'>Class: Testing</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L78'>Method: add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L247'>Method: copy_to</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L55'>Method: data_keys_add</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L169'>Method: get_all</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L127'>Method: get_all_parents</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L153'>Method: get_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L163'>Method: get_child_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L147'>Method: get_children</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L159'>Method: get_children_by_key_values</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L211'>Method: get_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L203'>Method: get_next_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L138'>Method: get_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L207'>Method: get_previous_sibling</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L187'>Method: get_siblings</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L51'>Method: hook_add_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L47'>Method: hook_create_post</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L46'>Method: hook_create_pre</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L52'>Method: hook_lose_child</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L50'>Method: hook_lose_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L49'>Method: hook_new_parent</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L48'>Method: hook_remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L53'>Method: hook_set_attribute</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L231'>Method: load</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L122'>Method: remove</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L293'>Method: repr_list</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L224'>Method: save</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L216'>Method: set_index</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L85'>Method: set_parent</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L251'>Method: view</a>
└─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L16'>Class: TreeDiagram</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L78'>Method: add</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L247'>Method: copy_to</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L55'>Method: data_keys_add</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L169'>Method: get_all</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L127'>Method: get_all_parents</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L153'>Method: get_child</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L163'>Method: get_child_by_key_values</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L147'>Method: get_children</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L159'>Method: get_children_by_key_values</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L211'>Method: get_index</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L203'>Method: get_next_sibling</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L138'>Method: get_parent</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L207'>Method: get_previous_sibling</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L187'>Method: get_siblings</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L51'>Method: hook_add_child</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L47'>Method: hook_create_post</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L46'>Method: hook_create_pre</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L52'>Method: hook_lose_child</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L50'>Method: hook_lose_parent</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L49'>Method: hook_new_parent</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L48'>Method: hook_remove</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L53'>Method: hook_set_attribute</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L231'>Method: load</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L122'>Method: remove</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L293'>Method: repr_list</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L224'>Method: save</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L216'>Method: set_index</a>
   ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L85'>Method: set_parent</a>
   └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master//generallibrary/generallibrary/diagram.py#L251'>Method: view</a>
</pre>

## Todos
| Module               | Message                                                           |
|:---------------------|:------------------------------------------------------------------|
| packager.py          | Allow github, pypi or local repo not to exist in any combination. |
| packager.py          | Generate a release history from commit history.                   |
| packager_markdown.py | Inherit future crawler class for pypi and github.                 |
| packager_markdown.py | Add footnote to readme with date and commit if specified.         |