import os
import json

class Charter:
	
	def __init__(self, userName, channelNumbers=[]):
		self.userName = userName
		self.channeNumbers = channelNumbers

	def getCurrentTime(self):
		pass

	def CurrentSchedule(self, masterScheduleList):
		file_path = 'resources/master/' + masterScheduleList
		
		with open(file_path) as Resouce_File:
			 master_schedule =  json.load(Resouce_File)
			 return master_schedule

print("Testing")

userName = "JC"
channelNumbers= [58574]

ts = Charter(userName, channelNumbers)
UserFilterSchedule = ts.CurrentSchedule('currentSchedule.json')

print(UserFilterSchedule)