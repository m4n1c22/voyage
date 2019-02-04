#
#
#	\File		     :	voyage_car_pool_controller.py
#	\Author	      	 : 	Sreeram Sadasivam
#	\Description	 :	Module contains the controller class for
#
#                       voyage car controller
#
import voyage_auth as auth
import voyage_common as common
from voyage_core import Voyage_Carpool as Car_Pool
import requests, json
import ssl

class Voyage_Carpool_Controller:
    def __init__(self):
        self.auth_obj = auth()
        self.__car_pool_obj = Car_Pool(self.auth_obj)

    def checkAvailableRides(self, src="Bonn", dest="Darmstadt", begin_date="2019-02-05", end_date="2019-02-14"):
        self.__car_pool_obj.checkAvailableRides(src, dest, begin_date, end_date)
