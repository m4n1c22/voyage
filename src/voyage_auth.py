#
#
#	\File		     :	voyage_auth.py
#	\Author	      	 : 	Sreeram Sadasivam
#	\Description	 :	Module contains the authentication for various APIs used
#                       within Voyage.
#
#

import requests, json
import ssl
import voyage_credentials as credentials

class Voyage_Auth:
    def __init__(self, auth_type="blablacar"):
        self.auth_type = auth_type
        if self.auth_type == "DB_timetable":
            self.token = credentials.db_timetable_TOKEN
            self.header={'Authorization':"Bearer "+str(self.token),'Content-Type':'application/xml'}
            print self.header
        if self.auth_type == "blablacar":
            self.api_key = credentials.blablacar_API_KEY
            self.header={'key':self.api_key,'Content-Type':'application/xml'}
