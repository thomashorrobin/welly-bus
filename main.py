#!/usr/bin/env python

import busstops
import liststops
import sys

subcmd = sys.argv[1]

if subcmd == "stop":
    busstops.printBusStopTimes(sys.argv[2])
elif subcmd == "list":
    liststops.listStops()
elif subcmd == "grep":
    busstops.grepBusStops(sys.argv[2])
else:
    busstops.printBusStopTimes(sys.argv[1])
