#!/usr/bin/env python

import gtk
import classParser
import classNotificationIcon
import gobject
import time
import os

import sys
sys.path.append(".")

#Interval to call verification function
CALLBACK_TIMEOUT = 5*60*1000 #one minute

#Full path of the executing script
BASE_PATH = os.path.dirname(os.path.abspath(sys.argv[0])) + "/"

class pyMonitor:

	#List to hold all NotificationIcons
	NotificationIcons = []

	#Creates the Parser object. It probes the urls.
	def __init__(self):
		
		self.objParser = classParser.Parser()

		print BASE_PATH

		#Load config
		self.Config = self.objParser.ParseJSON(BASE_PATH+'config.json')

		if not self.Config:
			print 'Unable to read config file.'
			sys.exit()

		#Number of addresses
		self.N = len(self.Config['sites'])

		#Creates icon objects
		for d in self.Config['sites']:
			#print 'Name: ', d['name']

			#Create a new Notification icon object and push
			objTmp = classNotificationIcon.NotificationIcon()
			objTmp.set_tooltip(d['name']+": initializing...")

			#Push into list
			self.NotificationIcons.append(objTmp)

	#Define the loopback function. This function will be called every 5 mins, and can change the 
	# icon images. This is needed because gtk.main() blocks.
	def Callback(self):

		for n in range(self.N):
			self.NotificationIcons[n].changeIconToBusy()
			self.NotificationIcons[n].set_tooltip(self.Config['sites'][n]['name']+": querying...")

			#Verify
			if self.objParser.Verify(self.Config['sites'][n]['name'],self.Config['sites'][n]['address']):

				#Set tooltip and icon to good
				self.NotificationIcons[n].set_tooltip( self.Config['sites'][n]['name'] + ": ON!\n@" + self.get_time())
				self.NotificationIcons[n].changeIconToGood()
			else:
				
				#Set tooltip and icon to bad
				self.NotificationIcons[n].set_tooltip( self.Config['sites'][n]['name'] + ": OFF!\n@" + self.get_time())
				self.NotificationIcons[n].changeIconToBad()

		#Should return True for the next iteration to happen
		return True

	def get_time(self):
		return time.strftime("%H:%M:%S", time.localtime())


if __name__ == '__main__':

	#Now we need to set the proper timer to run
	objpyMonitor = pyMonitor()

	#Calls immediately and sets the callback function to be called every CALLBACK_TIMEOUT
	objpyMonitor.Callback()
	gobject.timeout_add(CALLBACK_TIMEOUT, objpyMonitor.Callback)

	#Blocks!
	gtk.main()
