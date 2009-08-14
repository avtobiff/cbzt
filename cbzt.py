#!/usr/bin/env python

# This file is part of CBZT.
#
# CBZT is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CBZT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CBZT.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright © Per Andersson 2009

import getopt
import sys

import cbzt
from cbzt.exception import Usage


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)

        return cbzt.launch()

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "For help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
