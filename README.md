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
<a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager#L1'>Module: generalpackager</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github#L7'>Class: GitHub</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github#L20'>Method: api_url</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github#L48'>Method: get_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github#L35'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github#L24'>Method: get_website</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github#L54'>Method: set_description</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github#L41'>Method: set_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github#L30'>Method: set_website</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github#L16'>Method: url</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module#L5'>Class: LocalModule</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo#L9'>Class: LocalRepo</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo#L73'>Method: commit_and_push</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo#L25'>Method: get_git_exclude_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo#L37'>Method: get_local_repos</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo#L21'>Method: get_metadata_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo#L33'>Method: get_package_paths</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo#L17'>Method: get_readme_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo#L29'>Method: get_setup_path</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo#L53'>Method: get_todos</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo#L42'>Method: path_is_repo</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager#L18'>Class: Packager</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown#L39'>Method: configure_contents_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files#L7'>Method: generate_file</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files#L52'>Method: generate_git_exclude</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown#L74'>Method: generate_readme</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_files#L15'>Method: generate_setup</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown#L67'>Method: get_attributes_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown#L8'>Method: get_badges_dict</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata#L26'>Method: get_classifiers</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_markdown#L22'>Method: get_installation_markdown</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_metadata#L16'>Method: get_topics</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager#L48'>Method: setup_all</a>
│  └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager_github#L5'>Method: sync_github_metadata</a>
├─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi#L3'>Class: PyPI</a>
└─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager#L12'>Class: Testing</a>
   └─ <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager#L13'>Method: hello</a>
</pre>

## Todos
| Module               | Message                                                           |
|:---------------------|:------------------------------------------------------------------|
| packager.py          | Allow github, pypi or local repo not to exist in any combination. |
| packager.py          | Generate a release history from commit history.                   |
| packager_markdown.py | Inherit future crawler class for pypi and github.                 |
| packager_markdown.py | Add footnote to readme with date and commit if specified.         |