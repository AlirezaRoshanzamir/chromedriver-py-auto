import logging
import os
import shutil

from chromedriver_py_auto.binary_path import binary_path
from chromedriver_py_auto.chrome import extract_chrome_version
from chromedriver_py_auto.version import Version


def copy_binary() -> None:
    import chromedriver_py

    logging.error(
        'Copying "{}" to "{}".'.format(chromedriver_py.binary_path, binary_path)
    )
    shutil.copy2(chromedriver_py.binary_path, binary_path)
    stat = os.stat(chromedriver_py.binary_path)
    os.chown(binary_path, stat.st_uid, stat.st_gid)


def extract_requirement_specifier() -> str:
    chrome_version = Version.from_string(extract_chrome_version())
    version_specifier_template = os.getenv(
        "CHROMEDRIVER_PY_AUTO_VERSION_SPECIFIER_TEMPLATE", "=={major}.{minor}.{patch}.*"
    )
    return ("chromedriver-py" + version_specifier_template).format(
        major=chrome_version.major,
        minor=chrome_version.minor,
        patch=chrome_version.patch,
        build=chrome_version.build,
    )
