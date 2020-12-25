[![PyPI version shields.io](https://img.shields.io/pypi/v/generalpackager.svg)](https://pypi.org/project/generalpackager/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/generalpackager.svg)](https://pypi.python.org/pypi/generalpackager/)
[![Generic badge](https://img.shields.io/badge/platforms-Windows%20|%20Ubuntu%20|%20MacOS-blue.svg)](https://shields.io/)
[![workflow Actions Status](https://github.com/ManderaGeneral/generalpackager/workflows/workflow/badge.svg)](https://github.com/ManderaGeneral/generalpackager/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/ManderaGeneral/generalpackager.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ManderaGeneral/generalpackager/alerts/)

# Package: generalpackager
Tools for managing package metadata. [Test](#:~:text=generalpackager)

## Installation
```
pip install generalpackager
```
#### Extras
| Name    | Command                                | Extra packages                    |
|:--------|:---------------------------------------|:----------------------------------|
| testing | `pip install generalpackager[testing]` | `hello`, `there` and `foo`        |
| another | `pip install generalpackager[another]` | `omg` and `hello`                 |
| full    | `pip install generalpackager[full]`    | `hello`, `there`, `foo` and `omg` |

## Attributes of module generalpackager

| Module   | Name                                              | Type   |   Attributes | Explanation                                                           |
|:---------|:--------------------------------------------------|:-------|-------------:|:----------------------------------------------------------------------|
| repo     | [Barren](#Attributes-of-class-Barren)             | class  |            1 | Contains methods that don't require repository or installed packages. |
| repo     | [APILocalRepo](#Attributes-of-class-localRepo) | class  |           13 | All markdown specific repository methods.                             |

#### Attributes of class Barren

| Module   | Name       | Type   | Explanation                |
|:---------|:-----------|:-------|:---------------------------|
| repo     | get_badges | method | Get badge image urls text. |

#### Attributes of class APILocalRepo

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
| repo     | get_badges       | method   | Redirect to `Barren.get_badges`.         |
| repo     | get_description  | method   | Get description text.                    |
| repo     | get_install      | method   | Get install text.                        |
| repo     | get_todos        | method   | Search package files for to do comments. |

## Todo
 - `repo.py`
   - Plan hierarchy.
   - Publish this packages.
   - Make APIGitHub actions use this package with `shared` repo.
 - `__init__.py`
   - test
