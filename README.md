# generalpackager

## Navigation
<pre>
<a href='#generalpackager'>generalpackager</a>  
├─ <a href='#Table-of-contents'>Table of contents</a>  
├─ <a href='#Description'>Description</a>  
├─ <a href='#Badges'>Badges</a>  
├─ <a href='#Installation'>Installation</a>  
│  └─ <a href='#Extras'>Extras</a>  
├─ <a href='#Todos'>Todos</a>  
└─ <a href='#Public-attributes'>Public attributes</a>  
   └─ <a href='#Namespace'>Namespace</a>  
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
| Module      | Message                                                           |
|:------------|:------------------------------------------------------------------|
| packager.py | Inherit future crawler class for pypi and github.                 |
| packager.py | Allow github, pypi or local repo not to exist in any combination. |

## Public attributes

### Namespace
| Name                              | First line of documentation                             |
|:----------------------------------|:--------------------------------------------------------|
| [GitHub](#Class-GitHub)           | Tools to interface a GitHub Repository.                 |
| [LocalModule](#Class-LocalModule) | Tools to interface a Local Python Module.               |
| [LocalRepo](#Class-LocalRepo)     | Tools to help Path interface a Local Python Repository. |
| [Packager](#Class-Packager)       | Uses APIs to manage 'general' package.                  |
| PyPI                              | Tools to interface pypi.org.                            |

#### Class: GitHub
| Method          | First line of documentation                           |
|:----------------|:------------------------------------------------------|
| get_description | Get a string of description in the GitHub repository. |
| get_topics      | Get a list of topics in the GitHub repository.        |
| get_website     | Get website specified in repository details.          |
| set_description | Set a description for the GitHub repository.          |
| set_topics      | Set a list of topics for the GitHub repository.       |
| set_website     | Set a website for the GitHub repository.              |

#### Class: LocalModule
| Method                  | First line of documentation   |
|:------------------------|:------------------------------|
| get_attributes_markdown | Get attributes markdown.      |

#### Class: LocalRepo
| Method            | First line of documentation                                                                                       |
|:------------------|:------------------------------------------------------------------------------------------------------------------|
| commit_and_push   | Commit and push this local repo to GitHub.                                                                        |
| get_local_repos   | Return a list of local repos in given folder.                                                                     |
| get_metadata_path | Get a Path instance pointing to README, regardless if it exists.                                                  |
| get_package_paths | Get a list of Paths pointing to each folder containing a Python file in this local repo, aka `namespace package`. |
| get_readme_path   | Get a Path instance pointing to README, regardless if it exists.                                                  |
| get_todos         | Get a list of dicts containing cleaned up todos.                                                                  |
| path_is_repo      | Return whether this path is a local repo.                                                                         |

#### Class: Packager
| Method                         | First line of documentation                       |
|:-------------------------------|:--------------------------------------------------|
| generate_readme                | Create readme markdown object.                    |
| get_badges_dict                | Get badges as a dict.                             |
| get_installation_markdown      | Get install markdown.                             |
| get_table_of_contents_markdown | Get table of contents lines.                      |
| setup_all                      | Called by GitHub Actions when a commit is pushed. |
| sync_github_metadata           | Sync GitHub with local metadata.                  |