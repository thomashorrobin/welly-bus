import csv
import prettytable
import os.path

fname = "stops.csv"

def listStops():
    fileexists = os.path.isfile(fname)
    if not fileexists:
        print("You don't have any past searches")
        return
    f = open(fname, "r")
    tb = prettytable.from_csv(f)
    f.close()
    print(tb)