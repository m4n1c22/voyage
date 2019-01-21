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
