import requests
import json
import prettytable
import liststops

def grepBusStops(search_term):
	url = "https://www.metlink.org.nz/api/v1/StopSearch/" + search_term

	myResponse = requests.get(url)

	if(myResponse.ok):
		jData = json.loads(myResponse.content.decode())

		if(jData == None): # if no stop is found the api will return a json file containing "null"
			print("No stops matched: " + search_term)
			return
		
		tb = prettytable.PrettyTable(['Stop Number', 'Name'])
		
		for stop in jData:
		    tb.add_row([stop["Sms"], stop["Name"]])
		
		print(tb)
	else:
	  # If response code is not ok (200), print the resulting http error code with description
		myResponse.raise_for_status()

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
	elif(myResponse.status_code == 404):
		print(busstop + " is not a valid busstop according to Metlink. Please try again.")
	else:
		print("The server returned an error: " + str(myResponse.status_code))
