from __future__ import annotations

from dataclasses import dataclass
from functools import total_ordering
from typing import Tuple


@total_ordering
@dataclass
class Version:
    major: int
    minor: int = 0
    patch: int = 0
    build: int = 0

    @classmethod
    def from_string(cls, string: str) -> Version:
        parts = list(map(int, string.split(".")))

        if len(parts) < 1 or len(parts) > 4:
            raise AssertionError('The version string "{}" is invalid.'.format(string))

        return Version(
            major=parts[0],
            minor=parts[1] if len(parts) > 1 else 0,
            patch=parts[2] if len(parts) > 2 else 0,
            build=parts[3] if len(parts) > 3 else 0,
        )

    def to_tuple(self) -> Tuple[int, int, int, int]:
        return (self.major, self.minor, self.patch, self.build)

    def __lt__(self, other: Version) -> bool:
        return self.to_tuple() < other.to_tuple()

    def __str__(self) -> str:
        return ".".join(map(str, self.to_tuple()))

    def __repr__(self) -> str:
        return "Version({})".format(str(self))
