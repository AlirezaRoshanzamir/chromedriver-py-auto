import os
from sys import platform


def extract_chrome_version() -> str:
    if platform in ("linux", "linux2"):
        return _extract_version_from_executable("/usr/bin/google-chrome")
    elif platform == "darwin":
        return _extract_version_from_executable(
            "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
        )
    raise AssertionError('The platform "{}" is not supported.'.format(platform))


def _extract_version_from_executable(executable_path: str) -> str:
    return (
        os.popen("{} --version".format(executable_path))
        .read()
        .strip("Google Chrome ")
        .strip()
    )
