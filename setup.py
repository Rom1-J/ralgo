from setuptools import setup

with open("requirements.txt") as f:
    install_requires = f.read().split("\n")

setup(
    python_requires=">=3.9",
    install_requires=install_requires,
)
