def json_format(json_array):

	init = '{"x":0,"y":0},'
	heartRate = ''
	breathingRate = ''
	postureData = ''
	skinTemp = ''
	legend_name = ['HeartRate', 'BreathingRate', 'PostureData', 'SkinTemperature']

	for i in range(0,len(json_array)):
		heartRate += '{"x":'+ json_array[i].get("time_recorded")+',"y": '+json_array[i].get("heart_rate")+'},'	
		breathingRate += '{"x":'+ str(json_array[i].get("time_recorded"))+',"y": '+str(json_array[i].get("breathing_rate"))+'},'	
		postureData += '{"x": '+ str(json_array[i].get("time_recorded"))+',"y": '+str(json_array[i].get("posture"))+'},'	
		skinTemp += '{"x": '+ str(json_array[i].get("time_recorded"))+',"y": '+str(json_array[i].get("estimated_core_temperature"))+'},'	
	index = 0
	heartRate = '[{"values":[' + init + heartRate +'],"key":"'+legend_name[index]+'"}]'
	index = index + 1
	breathingRate = '[{"values":[' + init + breathingRate +'],"key":"'+legend_name[index]+'"}]'
	index = index + 1
	postureData = '[{"values":[' + init + postureData +'],"key":"'+legend_name[index]+'"}]'
	index = index + 1
	skinTemp = '[{"values":[' + init + skinTemp +'],"key":"'+legend_name[index]+'"}]'
	print heartRate
	print breathingRate
	print postureData
	print skinTemp
	return heartRate, breathingRate, postureData, skinTemp

json_array = [
	  {
		"user_name": "mshrimal",
		"heart_rate": "120",
		"time_recorded": "1970-01-01T15:28:23.044000Z",
		"time_received": "2015-04-12T04:32:53.042339Z",
		"breathing_rate": "23",
		"ecg": "12",
		"estimated_core_temperature": 32,
		"posture": 30
	  },
	  {
		"user_name": "mshrimal",
		
		"heart_rate": "0",
		"time_recorded": "1970-01-01T15:28:23.044000Z",
		"time_received": "2015-04-12T06:20:31.639728Z",
		"breathing_rate": 34,
		"ecg": 12,
		"estimated_core_temperature": 33,
		"posture": 60
	  },
	   {
		"user_name": "mshrimal",
		"heart_rate": "0",
		"time_recorded": "1970-01-01T15:28:23.044000Z",
		"time_received": "2015-04-21T00:30:10.734027Z",
		"breathing_rate": "-0.1",
		"ecg": "0.0008",
		"estimated_core_temperature": 36,
		"posture": 90
	  }
	]
hR, bR, pos, skinTem = json_format(json_array)
