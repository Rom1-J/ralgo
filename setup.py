import re

from setuptools import setup

with open("requirements.txt") as f:
    install_requires = f.read().split("\n")

with open("ralgo/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

with open("README.md") as f:
    readme = f.read()

setup(
    name="Ralgo",
    author="Romain J.",
    author_email="romain@gnous.eu",
    url="https://github.com/Rom1-J/ralgo/",
    version=version,
    description="PoC for an encoding/decoding algorithm using prime factor, transposed matrix and random",
    long_description=readme,
    packages=["ralgo", "ralgo.ext.compressor", "ralgo.ext.graphical"],
    python_requires=">=3.9",
    install_requires=install_requires,
)
