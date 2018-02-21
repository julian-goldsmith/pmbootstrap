"""
Copyright 2018 Oliver Smith

This file is part of pmbootstrap.

pmbootstrap is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pmbootstrap is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pmbootstrap.  If not, see <http://www.gnu.org/licenses/>.
"""
import tarfile


def apk(args, path):
    """
    Parse an Alpine Linux package (apk), and return its content as dictionary.

    returns: {"arch": "x86_64",
              "builddate": "1500000001",
              "commit": "",
              "datahash": "820b227d5cdafe7c54f4ecb6cfa4fdcc1b35967...",
              "depend": "so:libc.musl-x86_64.so.1",
              "license": "MIT",
              "origin": "hello-world",
              "packager": "Unknown",
              "pkgdesc": "hello world program to be built in the testsuite",
              "pkgname": "hello-world",
              "pkgver": "1-r4",
              "provides": "cmd:hello-world",
              "size": "20480",
              "url": "https://..."}
    """
    # Read all lines
    with tarfile.open(path, "r:gz") as tar:
        with tar.extractfile(tar.getmember(".PKGINFO")) as handle:
            lines = handle.readlines()

    # Parse all lines
    ret = {}
    for line in lines:
        line = line.decode()

        # Skip comments
        if line.startswith("#"):
            continue

        # 'key = value\n' line
        split = line.split(" = ", 1)
        key = split[0]
        value = split[1]
        ret[key] = value[:-1]

    return ret
