import os, sys
import gtk
import time

BASE_PATH = os.path.dirname(os.path.abspath(sys.argv[0])) + "/"

class NotificationIcon(gtk.StatusIcon):

	def __init__(self):

		gtk.StatusIcon.__init__(self)
		self.changeIconToBad()
		
		self.connect("popup-menu", self.right_click_event)

	def right_click_event(self, icon, button, time):
        	menu = gtk.Menu()
        	quit = gtk.MenuItem("Quit")
        	quit.connect("activate", gtk.main_quit)
        	menu.append(quit)
       		menu.show_all()
	        menu.popup(None, None, gtk.status_icon_position_menu, button, time, self)

	def changeIconToGood(self):
		self.set_from_file(BASE_PATH+"icons/good.png")

	def changeIconToBad(self):
		self.set_from_file(BASE_PATH+"icons/bad.png")
	
	def changeIconToBusy(self):
		self.set_from_file(BASE_PATH+"icons/busy.png")
