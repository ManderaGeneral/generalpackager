# generalpackager

## Navigation
<pre>
<a href='#generalpackager'>generalpackager</a>
├─ <a href='#Navigation'>Navigation</a>
├─ <a href='#Description'>Description</a>
├─ <a href='#Badges'>Badges</a>
├─ <a href='#Installation'>Installation</a>
│  └─ <a href='#Extras'>Extras</a>
├─ <a href='#Todos'>Todos</a>
└─ <a href='#Public-attributes'>Public attributes</a>
   ├─ <a href='#Direct-namespace'>Direct namespace</a>
   ├─ <a href='#Recursive-attributes-navigation'>Recursive attributes navigation</a>
   └─ <a href='#Namespace-attributes'>Namespace attributes</a>
      ├─ <a href='#Class-GitHub'>Class: GitHub</a>
      ├─ <a href='#Class-LocalModule'>Class: LocalModule</a>
      ├─ <a href='#Class-LocalRepo'>Class: LocalRepo</a>
      └─ <a href='#Class-Packager'>Class: Packager</a>
</pre>

## Description
Tools to interface GitHub, PyPI, local repos and local modules.

## Badges
| UnitTests                                                                                                                                                               | Alerts                                                                                                                                                                                | Commit                                                                                          | Release                                                                                                                    | Python                                                                                                                          | Operating System                                                                                                              |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [![workflow Actions Status](https://github.com/ManderaGeneral/generalpackager/workflows/workflow/badge.svg)](https://github.com/ManderaGeneral/generalpackager/actions) | [![Total alerts](https://img.shields.io/lgtm/alerts/g/ManderaGeneral/generalpackager.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ManderaGeneral/generalpackager/alerts/) | ![GitHub last commit](https://img.shields.io/github/last-commit/ManderaGeneral/generalpackager) | [![PyPI version shields.io](https://img.shields.io/pypi/v/generalpackager.svg)](https://pypi.org/project/generalpackager/) | [![PyPI pyversions](https://img.shields.io/pypi/pyversions/generalpackager.svg)](https://pypi.python.org/pypi/generalpackager/) | [![Generic badge](https://img.shields.io/badge/platforms-Windows%20%7C%20Ubuntu%20%7C%20MacOS-blue.svg)](https://shields.io/) |

## Installation
```
pip install generalpackager
```

### Extras
| Name    | Command                                | Extra packages             |
|:--------|:---------------------------------------|:---------------------------|
| testing | `pip install generalpackager[testing]` | `hello`, `there` and `foo` |
| another | `pip install generalpackager[another]` | `omg` and `hello`          |

## Todos
| Module          | Message                                                           |
|:----------------|:------------------------------------------------------------------|
| packager.py     | Inherit future crawler class for pypi and github.                 |
| packager.py     | Allow github, pypi or local repo not to exist in any combination. |
| local_module.py | Remove Namespaces if we get code links working.                   |

## Public attributes

### Direct namespace
| Name                              | Type   | Description                                             |
|:----------------------------------|:-------|:--------------------------------------------------------|
| [GitHub](#Class-GitHub)           | Class  | Tools to interface a GitHub Repository.                 |
| [LocalModule](#Class-LocalModule) | Class  | Tools to interface a Local Python Module.               |
| [LocalRepo](#Class-LocalRepo)     | Class  | Tools to help Path interface a Local Python Repository. |
| [Packager](#Class-Packager)       | Class  | Uses APIs to manage 'general' package.                  |
| PyPI                              | Class  | Tools to interface pypi.org.                            |

### Recursive attributes navigation
<pre>
Module: generalpackager <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/__init__.py#L0'>[Code]</a>
├─ <a href='#Class-GitHub'>Class: GitHub</a> <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L7'>[Code]</a>
│  ├─ Method: get_description <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L40'>[Code]</a>
│  ├─ Method: get_topics <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L27'>[Code]</a>
│  ├─ Method: get_website <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L16'>[Code]</a>
│  ├─ Method: set_description <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L46'>[Code]</a>
│  ├─ Method: set_topics <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L33'>[Code]</a>
│  └─ Method: set_website <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/github.py#L22'>[Code]</a>
├─ <a href='#Class-LocalModule'>Class: LocalModule</a> <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L5'>[Code]</a>
│  └─ Method: get_attributes_markdown <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_module.py#L34'>[Code]</a>
├─ <a href='#Class-LocalRepo'>Class: LocalRepo</a> <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L9'>[Code]</a>
│  ├─ Method: commit_and_push <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L65'>[Code]</a>
│  ├─ Method: get_local_repos <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L29'>[Code]</a>
│  ├─ Method: get_metadata_path <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L21'>[Code]</a>
│  ├─ Method: get_package_paths <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L25'>[Code]</a>
│  ├─ Method: get_readme_path <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L17'>[Code]</a>
│  ├─ Method: get_todos <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L45'>[Code]</a>
│  └─ Method: path_is_repo <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/local_repo.py#L34'>[Code]</a>
├─ <a href='#Class-Packager'>Class: Packager</a> <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L117'>[Code]</a>
│  ├─ Method: configure_table_of_contents_markdown <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L44'>[Code]</a>
│  ├─ Method: generate_readme <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L54'>[Code]</a>
│  ├─ Method: get_badges_dict <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L13'>[Code]</a>
│  ├─ Method: get_installation_markdown <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L27'>[Code]</a>
│  ├─ Method: setup_all <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L138'>[Code]</a>
│  └─ Method: sync_github_metadata <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/packager.py#L88'>[Code]</a>
└─ Class: PyPI <a href='https://github.com/ManderaGeneral/generalpackager/blob/master/generalpackager/api/pypi.py#L3'>[Code]</a>
</pre>

### Namespace attributes

#### Class: GitHub
| Name            | Type   | Description                                           |
|:----------------|:-------|:------------------------------------------------------|
| get_description | Method | Get a string of description in the GitHub repository. |
| get_topics      | Method | Get a list of topics in the GitHub repository.        |
| get_website     | Method | Get website specified in repository details.          |
| set_description | Method | Set a description for the GitHub repository.          |
| set_topics      | Method | Set a list of topics for the GitHub repository.       |
| set_website     | Method | Set a website for the GitHub repository.              |

#### Class: LocalModule
| Name                    | Type   | Description              |
|:------------------------|:-------|:-------------------------|
| get_attributes_markdown | Method | Get attributes markdown. |

#### Class: LocalRepo
| Name              | Type   | Description                                                                                                       |
|:------------------|:-------|:------------------------------------------------------------------------------------------------------------------|
| commit_and_push   | Method | Commit and push this local repo to GitHub.                                                                        |
| get_local_repos   | Method | Return a list of local repos in given folder.                                                                     |
| get_metadata_path | Method | Get a Path instance pointing to README, regardless if it exists.                                                  |
| get_package_paths | Method | Get a list of Paths pointing to each folder containing a Python file in this local repo, aka `namespace package`. |
| get_readme_path   | Method | Get a Path instance pointing to README, regardless if it exists.                                                  |
| get_todos         | Method | Get a list of dicts containing cleaned up todos.                                                                  |
| path_is_repo      | Method | Return whether this path is a local repo.                                                                         |

#### Class: Packager
| Name                                 | Type   | Description                                       |
|:-------------------------------------|:-------|:--------------------------------------------------|
| configure_table_of_contents_markdown | Method | Configure table of contents lines from markdown.  |
| generate_readme                      | Method | Create readme markdown object.                    |
| get_badges_dict                      | Method | Get badges as a dict.                             |
| get_installation_markdown            | Method | Get install markdown.                             |
| setup_all                            | Method | Called by GitHub Actions when a commit is pushed. |
| sync_github_metadata                 | Method | Sync GitHub with local metadata.                  |