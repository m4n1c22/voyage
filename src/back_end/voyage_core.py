#
#
#	\File		     :	voyage_core.py
#	\Author	      	 : 	Sreeram Sadasivam
#	\Description	 :	Module contains the core functions used
#                       within Voyage.
#
#
import voyage_auth as auth
import voyage_common as common
import requests, json
import ssl
import xml_parser

class Voyage_Coverage:
    def __init__(self, auth_obj):
        self.place_name = ""
        self.latitude = 0.0
        self.longitude = 0.0
        self.auth_obj = auth_obj

    def getCoverage(self):

        api_url = common.getNativiaAPIURL()
        # Login method
        request_url = api_url+"coverage"
        print (request_url)
        response = requests.get(request_url, headers=self.auth_obj.header,verify=False)
        print (response)
        print (response.json())

class Voyage_Station:
    def __init__(self, auth_obj):
        self.place_name = ""
        self.auth_obj = auth_obj

    def getStation(self,station_name=""):
        self.station_name = station_name

        api_url = common.getDBTimetableAPIURL()
        # Login method
        request_url = api_url+"station/"+self.station_name
        print (request_url)
        response = requests.get(request_url, headers=self.auth_obj.header,verify=False)
        ret_val = xml_parser.xml_to_json(response.content)
        print (ret_val)

class Voyage_DB:
    def __init__(self, auth_obj):
        self.auth_obj = None

#    def findClosestStation(self, stationName):


#    def checkConnectionsBetweenStations(self, source="Bonn", destination="Darmstadt",begin_date="2019-01-28",end_date="2019-02-01",number_of_seats=1):


class Voyage_Carpool:
    def __init__(self, auth_obj):
        self.auth_obj = auth_obj

    def checkAvailableRides(self, source="Bonn", destination="Darmstadt",begin_date="2019-02-02",end_date="2019-02-11",number_of_seats=1):
        api_url = common.getBlablacarAPIURL()
        request_url = api_url+"trips?fn="+source+"&tn="+destination+"&_format=json&cur=EUR&db="+begin_date+"&de="+end_date+"&seats="+str(number_of_seats)
        print (request_url)
        response = requests.get(request_url, headers=self.auth_obj.header,verify=False)

        trips = response.json()["trips"]
        #print (trips)
        avail_rides = []
        for trip in trips:
            ride = {}
            ride["from"] = trip["departure_place"]["address"]
            ride["to"] = trip["arrival_place"]["address"]
            avail_rides.append(ride)
        print avail_rides
