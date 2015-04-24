def json_format_heart_rate(json_array):
        heartRate = ''
        
        for i in range(0,len(json_array)):
            heartRate += '{"x":"'+ str(json_array[i].get("time_recorded"))+'","y": '+str(json_array[i].get("heart_rate"))+'},'      
        index = 0
        heartRate = heartRate.rstrip(',')
        heartRate = '[{"values":[' + heartRate +'],"key":"'+ 'HeartRate' +'"}]'
        return heartRate

def json_format_breathing_rate(json_array):
        breathingRate = ''
        
        for i in range(0,len(json_array)):
            breathingRate += '{"x":"'+ str(json_array[i].get("time_recorded"))+'","y": '+str(json_array[i].get("breathing_rate"))+'},'      
        breathingRate = breathingRate.rstrip(',')
        breathingRate = '[{"values":[' + breathingRate +'],"key":"'+ "BreathingRate"+'"}]'
        return breathingRate

def json_format_posture_rate(json_array):
        postureData = ''
        
        for i in range(0,len(json_array)):
            postureData += '{"x":"'+ str(json_array[i].get("time_recorded"))+'","y": '+str(json_array[i].get("posture"))+'},'       
        postureData = postureData.rstrip(',')
        postureData = '[{"values":[' + postureData +'],"key":"'+ "Posture Data" +'"}]'
        return postureData

def json_format_skin_temperature(json_array):
        print json_array
        skinTemp = ''
        for i in range(0,len(json_array)):
            skinTemp += '{"x":"'+ str(json_array[i].get("time_recorded"))+'","y": '+str(json_array[i].get("estimated_core_temperature"))+'},'       
        skinTemp = skinTemp.rstrip(',')
        skinTemp = '[{"values":[' + skinTemp +'],"key":"'+ "Skin Temperature" +'"}]'
        return skinTemp
