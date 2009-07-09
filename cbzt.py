#!/usr/bin/env python

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
