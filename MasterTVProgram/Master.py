import os
import json

class Master:
	
	def __init__(self, userName, channelList=None):
		self.userName = userName
		self.channeList = channelList

	def getCurrentTime(self):
		pass

	def CurrentSchedule(self, masterScheduleList):
		file_path = 'resources/master/' + masterScheduleList
		
		with open(file_path) as Resouce_File:
			 master_schedule =  json.load(Resouce_File)
			 return master_schedule

print("Testing")

ts = Master.CurrentSchedule('Test', 'currentSchedule.json')
print(ts)