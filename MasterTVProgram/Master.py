import os
import json

class Charter:
	
	def __init__(self, userName, channelNumbers=[]):
		self.userName = userName
		self.channeNumbers = channelNumbers

	def getCurrentTime(self):
		pass

	def getMasterSchedule(self, masterScheduleList):
		file_path = 'resources/master/' + masterScheduleList
		
		with open(file_path) as Resouce_File:
			 master_schedule =  json.load(Resouce_File)
			 return master_schedule

if __name__ == "__main__":
	from users import UserSchedule
	
	print("Testing")

	userName = "JC"
	channelNumbers= [58574,1]

	ts = Charter(userName, channelNumbers)
	masterSchedule = ts.getMasterSchedule('currentSchedule.json')

    # Instantiate User Class
	user =  UserSchedule.Users()
	#master_recorde_cnt =  user.RecordCnt(masterSchedule, 53, 1)
	#print(master_recorde_cnt)

	#userSchedule = user.GetUserSchedule(userName, masterSchedule, 53, 1)
	#print(userSchedule)

	#WriteUserSchedule = user.WriteUserSchedule(userName, userSchedule, 53, 1)
	#print("Write Success: " + WriteUserSchedule)

	ReadUserSchedule = user.ReadUserSchedule(userName, 1, 1)
	print(ReadUserSchedule)
	#