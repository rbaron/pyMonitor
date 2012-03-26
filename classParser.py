import urllib2
from urllib2 import HTTPError, URLError
import json

#Turn to True to output some stuff!
VERBOSE = False

#Timeout in seconds, for urlopen()
TIMEOUT = 10

class Parser:

	#Config: JSON object, nested:
	#{ 'sites': [ { 'name': 'name1', 'address': 'address1' }, { 'name': 'name2', 'address': 'address2' } ] }

	#Returns a dict
	def ParseJSON(self, filename):
		try:
			fp = open(filename, 'r')
			self.Config = json.load(fp)
			return self.Config
		except:
			if VERBOSE: "Failed to load config."
			return False

	def Verify(self, name, address):

		try:
			urllib2.urlopen(address, None, TIMEOUT)

		except HTTPError, e:
			if VERBOSE: print "HTTPError: code: ", e.code
			return False

		except URLError, e:
			if VERBOSE: print "URLError: ", e.reason
			return False
		else:
			return True
