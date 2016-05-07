import requests
import json
import prettytable
import liststops

def printBusStopTimes(busstop):
	url = "https://www.metlink.org.nz/api/v1/StopDepartures/" + str(busstop)

	myResponse = requests.get(url)

	if(myResponse.ok):
		jData = json.loads(myResponse.content.decode())

		stopName = jData["Stop"]["Name"]
		stopNumber = jData["Stop"]["Sms"]
		farezone = jData["Stop"]["Farezone"]

		print("\n")
		print(stopName)

		tb = prettytable.PrettyTable(['Bus No', 'Destination', 'Est departure'])

		for service in jData["Services"]:
		    departTime = divmod(int(service["DisplayDepartureSeconds"]), 60)
		    tb.add_row([service["ServiceID"], service["DestinationStopName"], str(departTime[0]) + "mins " + str(departTime[1]) + "secs"])

		print(tb)
		print("\n")

		liststops.addStopToList(stopNumber, stopName, farezone)
	else:
	  # If response code is not ok (200), print the resulting http error code with description
		myResponse.raise_for_status()
