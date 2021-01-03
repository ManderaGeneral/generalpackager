
from setuptools import setup, find_namespace_packages
from pathlib import Path

setup(
    name="generalpackager",
    author='Rickard "Mandera" Abraham',
    author_email="rickard.abraham@gmail.com",
    version="0.0.2",
    description="Tools to interface GitHub, PyPI and local modules / repos. Used for generating files to keep projects dry and synced.",
    long_description=Path(r'C:\Python\Repos\generalpackager\README.md').read_text(),
    long_description_content_type="text/markdown",
    install_requires=[
        'generalfile',
        'generallibrary',
        'pandas',
        'requests',
        'gitpython',
        'wheel',
        'twine',
    ],
    url="https://github.com/ManderaGeneral/generalpackager",
    license="mit",
    python_requires="==3.8.*, ==3.9.*",
    packages=find_namespace_packages(),
    extras_require={},
    classifiers=[
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
    ],
)
