
from setuptools import setup, find_namespace_packages
from pathlib import Path

setup(
    name="generalpackager",
    author='Rickard "Mandera" Abraham',
    version="0.0.1",
    description="Tools to interface GitHub, PyPI and local modules / repos. Used for generating files to keep projects dry and synced.",
    long_description=Path(r'C:\Python\Repos\generalpackager\README.md').read_text(),
    install_requires=['generalfile', 'generallibrary', 'pandas', 'requests', 'gitpython'],
    url="https://github.com/ManderaGeneral/generalpackager",
    license="mit-license",
    python_requires="==3.8.*, ==3.9.*",
    packages=find_namespace_packages(),
    extras_require={'testing': ['hello', 'there', 'foo'], 'another': ['omg', 'hello']},
    classifiers=['Topic :: Software Development :: Build Tools', 'Programming Language :: Python :: 3.8', 'Topic :: Software Development :: Libraries'],
)
