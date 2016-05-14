import csv
import prettytable
import os.path

fname = "~/.metlink-stops.csv"
fileexists = os.path.isfile(fname)

def listStops():
    if not fileexists:
        print("You don't have any past searches")
        return
    f = open(fname, "r")
    tb = prettytable.from_csv(f)
    f.close()
    print(tb)
    
def addStopToList(number, name, fare_zone):
    csvList = [["Stop Number","Name","Fare Zone"],[number,name,fare_zone]]
    if fileexists:
        with open('stops.csv', 'r') as f:
            reader = csv.reader(f)
            stops_in_file_list = list(reader)
            for s in stops_in_file_list[1:]:
                if s[0] != number:
                    csvList.append([s[0], s[1], s[2]])
    with open('stops.csv', 'w') as f:
        wr = csv.writer(f)
        wr.writerows(csvList)
        