import logging
from pathlib import Path

import setuptools
from setuptools.command.build_py import build_py

from chromedriver_py_auto import install

logging.basicConfig(level=logging.INFO)


class InstallSuitableChromedriverPy(setuptools.command.build_py.build_py):
    def run(self) -> None:
        install()
        build_py.run(self)


setuptools.setup(
    name="chromedriver-py-auto",
    version="0.2.0",
    description="A wrapper around chromedriver-py library. Detects the Chrome version "
    "and installs the most suitable chromedriver-py version.",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    license="MIT License",
    author="Alireza Roshanzamir",
    author_email="a.roshanzamir1996@gmail.com",
    url="https://github.com/AlirezaRoshanzamir/chromedriver-py-auto",
    packages=setuptools.find_packages(),
    include_package_data=True,
    cmdclass={"build_py": InstallSuitableChromedriverPy},
)
