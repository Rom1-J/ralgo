import os
from collections import namedtuple

__version__ = "2.0.0a"

build = os.popen("/usr/bin/git rev-parse --short HEAD").read().strip()
info = os.popen('/usr/bin/git log -n 3 -s --format="%s"').read().strip()

VersionInfo = namedtuple(
    "VersionInfo", "major minor micro release_level build, info"
)
version_info = VersionInfo(
    major=2, minor=0, micro=0, release_level="alpha", build=build, info=info
)

version_info = "v{}.{}.{}-{}.{}".format(  # pylint: disable=invalid-name
    version_info.major,
    version_info.minor,
    version_info.micro,
    version_info.release_level,
    version_info.build,
).replace("\n", "")
