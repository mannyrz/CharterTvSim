import os
import json
import random


class Users:

	def RecordCnt(self, scheduleMaster, userChannelNumber, userChannelId):
		return len(scheduleMaster)

	def GetUserSchedule(self, userName, scheduleMaster, userChannelNumber, userChannelId):
		userScheduleList = []
		for x in range(4):
			userScheduleList.append(scheduleMaster[x]) # add random
	 	
		# for x in range(len(userScheduleList)):
		#  	print(userScheduleList[x])
			
		return userScheduleList

	def WriteUserSchedule(self, userName, userScheduleList, userChannelNumber, userChannelId):
		#Convert list to a json object
		userSchedule = json.dumps(userScheduleList)
		
		filepath = 'resources/users/' + userName + '-userScheduleList.json'
		
		with open(filepath, 'w') as outfile:
			json.dump(userSchedule, outfile, ensure_ascii=False, indent=4)
		
		return True
	
	def ReadUserSchedule(self, userName, userChannelNumber, userChannelId):
	
		filepath = 'resources/users/' + userName + '-userScheduleList.json'
		
		with open(filepath) as Resouce_File:
			 user_schedule =  json.load(Resouce_File)
		return user_schedule