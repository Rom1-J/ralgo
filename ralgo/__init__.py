import os
from collections import namedtuple

__version__ = "2.0.0a"

build = os.popen("/usr/bin/git rev-parse --short HEAD").read().strip()
info = os.popen('/usr/bin/git log -n 3 -s --format="%s"').read().strip()

VersionInfoBuilder = namedtuple(
    "VersionInfoBuilder", "major minor micro release_level build, info"
)
version_info_data = VersionInfoBuilder(
    major=2, minor=0, micro=0, release_level="alpha", build=build, info=info
)

version_info = "v{}.{}.{}-{}.{}".format(  # pylint: disable=invalid-name
    version_info_data.major,
    version_info_data.minor,
    version_info_data.micro,
    version_info_data.release_level,
    version_info_data.build,
).rstrip()
