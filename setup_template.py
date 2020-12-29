
from setuptools import setup, find_namespace_packages


setup(
    author='Rickard "Mandera" Abraham',
    url=f"https://github.com/ManderaGeneral/{ cfg('setup', 'name') }",
    license="MIT",
    python_requires=">= 3.8, < 3.10",
    packages=find_namespace_packages(),

    name=cfg("setup", "name"),
    version=cfg("setup", "version"),
    description=cfg("setup", "description"),

    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=classifiers,
)
