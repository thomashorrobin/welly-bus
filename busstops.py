import requests
import json

def printBusStopTimes(busstop):
	url = "https://www.metlink.org.nz/api/v1/StopDepartures/" + str(busstop)

	myResponse = requests.get(url)

	if(myResponse.ok):
		jData = json.loads(myResponse.content.decode())

		print(jData["Stop"]["Name"] + "(" + jData["Stop"]["Sms"] + ")")

		for service in jData["Services"]:
		    sec = int(service["DisplayDepartureSeconds"])
		    minutes =  round(sec / 60)
		    print('{0} ({2}min) {1}'.format(service["ServiceID"],service["DestinationStopName"],minutes))
	else:
	  # If response code is not ok (200), print the resulting http error code with description
		myResponse.raise_for_status()