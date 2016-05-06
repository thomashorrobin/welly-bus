import requests
import json
import prettytable

def printBusStopTimes(busstop):
	url = "https://www.metlink.org.nz/api/v1/StopDepartures/" + str(busstop)

	myResponse = requests.get(url)

	if(myResponse.ok):
		jData = json.loads(myResponse.content.decode())

		print(jData["Stop"]["Name"] + "(" + jData["Stop"]["Sms"] + ")")
		
		tb = prettytable.PrettyTable(['Bus No', 'Destination', 'Est departure'])
		
		for service in jData["Services"]:
		    departTime = divmod(int(service["DisplayDepartureSeconds"]), 60)
		    tb.add_row([service["ServiceID"], service["DestinationStopName"], str(departTime[0]) + "mins " + str(departTime[1]) + "secs"])
		
		print(tb)
	else:
	  # If response code is not ok (200), print the resulting http error code with description
		myResponse.raise_for_status()