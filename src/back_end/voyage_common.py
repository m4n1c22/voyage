#
#
#	\File		     :	voyage_common.py
#	\Author	      	 : 	Sreeram Sadasivam
#	\Description	 :	Module contains the common functions and contants
#                       within Voyage.
#
#

def getNativiaAPIURL():
    navitia_api_url = "http://api.navitia.io/v1/"
    return navitia_api_url


def getDBTimetableAPIURL():
    db_timetable_api_url = "https://api.deutschebahn.com/timetables/v1/"
    return db_timetable_api_url

def getBlablacarAPIURL():
    blablacar_api_url = "https://public-api.blablacar.com/api/v2/"
    return blablacar_api_url

def getOpenBahnAPIURL():
    openbahn_api_url = ""
    return openbahn_api_url
