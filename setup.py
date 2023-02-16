import logging
from pathlib import Path

import setuptools
import setuptools.command.install

from chromedriver_py_auto import install

logging.basicConfig(level=logging.INFO)


class InstallSuitableChromedriverPy(setuptools.command.install.install):
    def run(self) -> None:
        super().run()
        install()


setuptools.setup(
    name="chromedriver-py-auto",
    version="0.1.0",
    description="A wrapper around chromedriver-py library. Detects the Chrome version "
    "and installs the most suitable chromedriver-py version.",
    long_description=Path("README.md").read_text(),
    license=Path("LICENSE").read_text(),
    author="Alireza Roshanzamir",
    author_email="a.roshanzamir1996@gmail.com",
    url="https://github.com/AlirezaRoshanzamir/chromedriver-py-auto",
    packages=setuptools.find_packages(),
    cmdclass={"install": InstallSuitableChromedriverPy},
)
