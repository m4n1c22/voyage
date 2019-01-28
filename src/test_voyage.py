#
#
#	\File		     :	test_voyage.py
#	\Author	      	 : 	Sreeram Sadasivam
#	\Description	 :	Test program to verify the functionality of voyage APIs
#
#

import requests, json
import ssl
from voyage_auth import Voyage_Auth as auth
from voyage_core import Voyage_Coverage as coverage
from voyage_core import Voyage_Station as station
from voyage_core import Voyage_Carpool as carpool
class Voyage_Test:

    def __init__(self):
        self.auth_obj = auth()
        #self.coverage_obj = coverage(self.auth_obj)
        #self.station_obj = station(self.auth_obj)
        self.carpool_obj = carpool(self.auth_obj)
    #def test_coverage_nets(self):
    #    self.coverage_obj.getCoverage()

    def test_station(self):
        self.station_obj.getStation("BLS")

    def test_check_available_rides(self):
        self.carpool_obj.checkAvailableRides()

if __name__ == '__main__':

    test_obj = Voyage_Test()
    #test_obj.test_coverage_nets()
    test_obj.test_check_available_rides()
