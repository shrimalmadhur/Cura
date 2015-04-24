def json_format(json_array):

	#init = '{"x":0,"y":0},'
	heartRate = ''
	breathingRate = ''
	postureData = ''
	skinTemp = ''
	legend_name = ['HeartRate', 'BreathingRate', 'PostureData', 'SkinTemperature']
	
	for i in range(0,len(json_array)):
		if json_array[i].get("time_recorded") 
		heartRate += '{"x":"'+ str(json_array[i].get("time_recorded"))+'","y": '+str(json_array[i].get("heart_rate"))+'},'	
		breathingRate += '{"x":"'+ str(json_array[i].get("time_recorded"))+'","y": '+str(json_array[i].get("breathing_rate"))+'},'	
		postureData += '{"x":"'+ str(json_array[i].get("time_recorded"))+'","y": '+str(json_array[i].get("posture"))+'},'	
		skinTemp += '{"x":"'+ str(json_array[i].get("time_recorded"))+'","y": '+str(json_array[i].get("estimated_core_temperature"))+'},'	
	index = 0
	heartRate = heartRate.rstrip(',')
	breathingRate = breathingRate.rstrip(',')
	postureData = postureData.rstrip(',')
	skinTemp = skinTemp.rstrip(',')
	heartRate = '[{"values":[' + heartRate +'],"key":"'+legend_name[index]+'"}]'
	index = index + 1
	breathingRate = '[{"values":[' + breathingRate +'],"key":"'+legend_name[index]+'"}]'
	index = index + 1
	postureData = '[{"values":[' + postureData +'],"key":"'+legend_name[index]+'"}]'
	index = index + 1
	skinTemp = '[{"values":[' + skinTemp +'],"key":"'+legend_name[index]+'"}]'
	print heartRate
	print breathingRate
	print postureData
	print skinTemp
	return heartRate, breathingRate, postureData, skinTemp
json_array =[
  {
    "id": 8,
    "user_name": "mshrimal",
    "time_recorded": "1970-01-17T13:10:25.857000Z",
    "time_received": "2015-04-24T02:44:59.478681Z",
    "weight": 74980000
  },
  {
    "id": 9,
    "user_name": "mshrimal",
    "time_recorded": "1970-01-17T13:10:25.857000Z",
    "time_received": "2015-04-24T02:47:00.449079Z",
    "weight": 75
  },
  {
    "id": 10,
    "user_name": "mshrimal",
    "time_recorded": "2015-04-23T21:50:57Z",
    "time_received": "2015-04-24T02:49:57.914047Z",
    "weight": 75
  },
  {
    "id": 11,
    "user_name": "mshrimal",
    "time_recorded": "2015-04-23T21:50:57Z",
    "time_received": "2015-04-24T02:50:56.111584Z",
    "weight": 75
  },
  {
    "id": 12,
    "user_name": "mshrimal",
    "time_recorded": "2015-04-23T21:50:57Z",
    "time_received": "2015-04-24T02:51:09.650433Z",
    "weight": 75
  },
  {
    "id": 13,
    "user_name": "mshrimal",
    "time_recorded": "2015-04-23T21:50:57Z",
    "time_received": "2015-04-24T02:53:04.114558Z",
    "weight": 75
  },
  {
    "id": 14,
    "user_name": "mshrimal",
    "time_recorded": "2015-04-23T21:50:57Z",
    "time_received": "2015-04-24T02:53:09.364948Z",
    "weight": 75
  },
  {
    "id": 15,
    "user_name": "mshrimal",
    "time_recorded": "2015-04-23T21:50:57Z",
    "time_received": "2015-04-24T02:53:15.040279Z",
    "weight": 75
  }
]
hR, bR, pos, skinTem = json_format(json_array)
