def json_format(json_array):
	# json_array Response from http://128.2.83.208:8004/docs/#!/bloodoxygen/Blood_Oxygen_By_User
	#init = '{"x":0,"y":0},'
	bloodoxygen = ''
	legend_name = ['BloodOxygen']
	
	for i in range(0,len(json_array)):
		bloodoxygen += '{"x":"'+ str(json_array[i].get("time_recorded"))+'","y": '+str(json_array[i].get("blood_oxygen"))+'},'	
	index = 0
	bloodoxygen = bloodoxygen.rstrip(',')
	bloodoxygen = '[{"values":[' + bloodoxygen +'],"key":"'+legend_name[index]+'"}]'
	print bloodoxygen
	return bloodoxygen
	
# json_array =[
  # {
    # "id": 1,
    # "user_name": "sravya",
    # "blood_oxygen": 50,
    # "timestamp_year": 1992,
    # "timestamp_month": 0,
    # "timestamp_day": 0,
    # "timestamp_msofday": 0,
    # "time_recorded": "2015-04-23T21:50:57Z"
  # },
  # {
    # "id": 2,
    # "user_name": "sravya",
    # "blood_oxygen": 56,
    # "timestamp_year": 78,
    # "timestamp_month": 65,
    # "timestamp_day": 0,
    # "timestamp_msofday": 0,
    # "time_recorded": "2015-04-24T21:50:57Z"
  # }
# ]
w = json_format(json_array)
