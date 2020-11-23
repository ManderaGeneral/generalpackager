[![PyPI version shields.io](https://img.shields.io/pypi/v/generalpackager.svg)](https://pypi.org/project/generalpackager/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/generalpackager.svg)](https://pypi.python.org/pypi/generalpackager/)
[![Generic badge](https://img.shields.io/badge/platforms-Windows%20|%20Ubuntu%20|%20MacOS-blue.svg)](https://shields.io/)
[![workflow Actions Status](https://github.com/ManderaGeneral/generalpackager/workflows/workflow/badge.svg)](https://github.com/ManderaGeneral/generalpackager/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/ManderaGeneral/generalpackager.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ManderaGeneral/generalpackager/alerts/)

# Package: generalpackager
Easily manage packages cross platform.

## Installation
```
pip install generalpackager
```

## Attributes of module generalpackager

| Module   | Name                                              | Type   |   Attributes | Explanation                               |
|:---------|:--------------------------------------------------|:-------|-------------:|:------------------------------------------|
| repo     | [RepoMarkdown](#Attributes-of-class-RepoMarkdown) | class  |           13 | All markdown specific repository methods. |

#### Attributes of class RepoMarkdown

| Module   | Name             | Type     | Explanation                              |
|:---------|:-----------------|:---------|:-----------------------------------------|
|          | classifiers      | variable | Variable of type 'ellipsis'.             |
|          | description      | variable | Variable of type 'ellipsis'.             |
|          | extras_require   | variable | Variable of type 'ellipsis'.             |
|          | full             | variable | Variable of type 'ellipsis'.             |
|          | install_requires | variable | Variable of type 'ellipsis'.             |
|          | name             | variable | Variable of type 'ellipsis'.             |
|          | version          | variable | Variable of type 'ellipsis'.             |
| repo     | create_readme    | method   | Create README.                           |
| repo     | get_attributes   | method   | Get attributes text.                     |
| repo     | get_badges       | method   | Get badge image urls text.               |
| repo     | get_description  | method   | Get description text.                    |
| repo     | get_install      | method   | Get install text.                        |
| repo     | get_todos        | method   | Search package files for to do comments. |

## Todo
 - repo.py
   - Plan hierarchy.
   - Categorize methods into classes, `get_badges` doesn't require a cloned repository for example.
   - Publish this packages.
   - Make GitHub actions use this package with `shared` repo.