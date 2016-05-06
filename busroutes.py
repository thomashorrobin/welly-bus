import requests
import json

def printBusRouteInfo(route):
	url = "https://www.metlink.org.nz/api/v1/ServiceLocation/" + str(route)

	myResponse = requests.get(url)

	if(myResponse.ok):
		jData = json.loads(myResponse.content.decode())
        print("successfully recived date from " + url)