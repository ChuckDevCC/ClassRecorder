import schedule
import time
import win32com.client as client
import win32api
import os
# important libraries to do the magic

# bind the library to an easy variable
shell = client.Dispatch("WScript.Shell")

# our function for the first class.
# This one will open OBS and keep it open
# for the rest of the classes for the day.
def firstClass():

	# not changing the directories
	# to where OBS is, causes errors.
	# edit the directory to where OBS 
	# is installed .
	os.chdir("D:\\Program Files\\obs-studio\\bin\\64bit")
	win32api.ShellExecute(0, 'open', 'D:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe', '', '', 1)
	time.sleep(5)

	# change F9 to your hotkey
	# for recording start in OBS
	shell.SendKeys("{F9}", 0)
	time.sleep(2)

	# changing directories to chrome folder
	os.chdir("C:\\Program Files (x86)\\Google\\Chrome\\Application")
	win32api.ShellExecute(0, 'open', 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe', '', '', 1)
	time.sleep(2)

	#placeholder, but will
	# be the URL for Zoom potentially
	shell.SendKeys("zoom.us")

def secondClass():
	
	#start recording
	shell.SendKeys("{F9}", 0)
	time.sleep(2)

	# changing directories to chrome folder
	os.chdir("C:\\Program Files (x86)\\Google\\Chrome\\Application")
	win32api.ShellExecute(0, 'open', 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe', '', '', 1)
	time.sleep(2)

	#placeholder, but will
	# be the URL for Zoom nneds
	shell.SendKeys("zoom.us")

def stop():

	# close the chrome tab
	shell.SendKeys("^w")
	time.sleep(2)
	# rebind for stop hotkey in OBS
	shell.SendKeys("{F10}", 1)


# using the schedule library
# set your time, using military time,
# a couple minutes before class start.
# repeat for x number of classes. (?)
schedule.every().monday.at("10:28").do(firstClass)
schedule.every().monday.at("11:22").do(stop)

schedule.every().monday.at("13:28").do(secondClass)
schedule.every().monday.at("14:22").do(stop)

schedule.every().tuesday.at("9:58").do(firstClass)
schedule.every().tuesday.at("11:17").do(stop)

schedule.every().wednesday.at("10:28").do(firstClass)
schedule.every().wednesday.at("11:22").do(stop)

schedule.every().wednesday.at("13:28").do(secondClass)
schedule.every().wednesday.at("14:22").do(stop)

schedule.every().thursday.at("9:58").do(firstClass)
schedule.every().thursday.at("11:17").do(stop)

schedule.every().friday.at("10:28").do(firstClass)
schedule.every().friday.at("11:22").do(stop)

schedule.every().friday.at("13:28").do(secondClass)
schedule.every().friday.at("14:22").do(stop)
# run the program to continue all scheduled tasks.
while True:
	schedule.run_pending()
	time.sleep(1)