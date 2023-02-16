import json
import logging
import urllib.request
from typing import Iterable, List, Optional

try:
    from pip import main as pip_main
except ImportError:
    from pip._internal import main as pip_main

from chromedriver_py_auto.chrome import extract_chrome_version
from chromedriver_py_auto.version import Version


def install() -> None:
    chrome_version = Version.from_string(extract_chrome_version())
    logging.info('Chrome version "{}" is detected.'.format(str(chrome_version)))

    chromedriver_py_versions = _get_package_versions("chromedriver-py")
    logging.info(
        'Chromedriver "{}" versions are found.'.format(
            '", "'.join(map(str, chromedriver_py_versions))
        )
    )

    most_suitable_chromedriver_py_version = _find_most_suitable_driver_version(
        chrome_version, chromedriver_py_versions
    )
    logging.info(
        'Chromedriver version "{}" is selected for installation.'.format(
            str(most_suitable_chromedriver_py_version)
        )
    )

    pip_main(
        [
            "install",
            "chromedriver-py=={}".format(most_suitable_chromedriver_py_version),
        ]
    )


def _get_package_versions(package_name: str) -> List[Version]:
    url = "https://pypi.org/pypi/%s/json" % (package_name,)
    data = json.load(urllib.request.urlopen(url))
    return sorted(map(Version.from_string, data["releases"]))


def _find_most_suitable_driver_version(
    software_version: Version, driver_versions: Iterable[Version]
) -> Version:
    sorted_driver_versions = sorted(driver_versions)
    pre_driver_version: Optional[Version] = None
    for driver_version in sorted_driver_versions:
        if software_version == driver_version:
            return driver_version
        elif software_version < driver_version:
            if software_version.major == driver_version.major:
                return driver_version
            elif (
                pre_driver_version is not None
                and software_version.major == pre_driver_version.major
            ):
                return pre_driver_version
            break
        pre_driver_version = driver_version

    raise ValueError(
        'For "{}" software version, there is no suitable driver '
        'version in "{}" list.'.format(
            software_version, '", "'.join(map(str, sorted_driver_versions))
        )
    )
