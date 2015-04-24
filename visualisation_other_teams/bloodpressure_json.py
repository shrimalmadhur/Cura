def json_format(json_array):
	# json_array Response from http://128.2.83.208:8004/docs/#!/bloodpressure/Blood_Oxygen_By_User
	#init = '{"x":0,"y":0},'
	systolic = ''
	dystolic = ''
	legend_name = ['systolic', 'dystolic']
	
	for i in range(0,len(json_array)):
		systolic += '{"x":"'+ str(json_array[i].get("time_recorded"))+'","y": '+str(json_array[i].get("systolic"))+'},'	
		dystolic += '{"x":"'+ str(json_array[i].get("time_recorded"))+'","y": '+str(json_array[i].get("dystolic"))+'},'	
	systolic = systolic.rstrip(',')
	dystolic = dystolic.rstrip(',')
	result = '[{"values":[' + systolic +'],"key":"'+legend_name[0]+'"},{"values":['+dystolic+'],"key":"'+legend_name[1]+'"}]'
	print result
	return result
	


# json_array = [
  # {
    # "id": 1,
    # "user_name": "sravya",
    # "systolic": 10,
    # "dystolic": 10,
    # "pulse": 10,
    # "timestamp_year": 10,
    # "timestamp_month": 10,
    # "timestamp_day": 10,
    # "timestamp_msofday": 10,
    # "time_recorded": 10
  # }
# ]
bp = json_format(json_array)
