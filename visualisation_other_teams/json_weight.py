def json_format(json_array):
	# json_array Response from http://128.2.83.208:8001/docs/#!/bloodpressure/Blood_Pressure_By_User
	#init = '{"x":0,"y":0},'
	weight = ''
	legend_name = ['Weight']
	
	for i in range(0,len(json_array)):
		weight += '{"x":"'+ str(json_array[i].get("time_recorded"))+'","y": '+str(json_array[i].get("weight"))+'},'	
	index = 0
	weight = weight.rstrip(',')
	weight = '[{"values":[' + weight +'],"key":"'+legend_name[index]+'"}]'
	print weight
	return weight
	
# json_array =[
  # {
    # "id": 8,
    # "user_name": "mshrimal",
    # "time_recorded": "1970-01-17T13:10:25.857000Z",
    # "time_received": "2015-04-24T02:44:59.478681Z",
    # "weight": 74980000
  # },
  # {
    # "id": 9,
    # "user_name": "mshrimal",
    # "time_recorded": "1970-01-17T13:10:25.857000Z",
    # "time_received": "2015-04-24T02:47:00.449079Z",
    # "weight": 75
  # },
  # {
    # "id": 10,
    # "user_name": "mshrimal",
    # "time_recorded": "2015-04-23T21:50:57Z",
    # "time_received": "2015-04-24T02:49:57.914047Z",
    # "weight": 75
  # },
  # {
    # "id": 11,
    # "user_name": "mshrimal",
    # "time_recorded": "2015-04-23T21:50:57Z",
    # "time_received": "2015-04-24T02:50:56.111584Z",
    # "weight": 75
  # },
  # {
    # "id": 12,
    # "user_name": "mshrimal",
    # "time_recorded": "2015-04-23T21:50:57Z",
    # "time_received": "2015-04-24T02:51:09.650433Z",
    # "weight": 75
  # },
  # {
    # "id": 13,
    # "user_name": "mshrimal",
    # "time_recorded": "2015-04-23T21:50:57Z",
    # "time_received": "2015-04-24T02:53:04.114558Z",
    # "weight": 75
  # },
  # {
    # "id": 14,
    # "user_name": "mshrimal",
    # "time_recorded": "2015-04-23T21:50:57Z",
    # "time_received": "2015-04-24T02:53:09.364948Z",
    # "weight": 75
  # },
  # {
    # "id": 15,
    # "user_name": "mshrimal",
    # "time_recorded": "2015-04-23T21:50:57Z",
    # "time_received": "2015-04-24T02:53:15.040279Z",
    # "weight": 75
  # }
# ]
w = json_format(json_array)
