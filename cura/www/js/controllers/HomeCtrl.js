angular.module('starter.controllers')
.controller('HomeCtrl', function ($scope, $http, $timeout) {
    var url = "http://128.2.83.208:8001/api/v1/homeautomation/ha_user/";
    $scope.switches = [];
    $scope.thermostat;

    $http.get(url).success(function(devices){
        for (id in devices){
            var device = devices[id];
            if (device.signal_type === "switch"){
                $scope.switches.push({ name: device.tag_id, isOn: device.required_value === "1" ? true : false});
            } else if (device.signal_type === "thermo"){
                var temp = parseInt(device.required_value, 16)/2;
                $scope.thermostat = {name: device.tag_id, temp: temp, isHeating: device.mode === "hot" ? true : false};
            }
        }
    });

    // Temp String Format
    $scope.tempMode = function(){
        if($scope.thermostat){
            return $scope.thermostat.isHeating?"Heating":"Cooling";
        }
        return "";
    }
    $scope.switchToggle = function(switchData){
/*        console.log(JSON.stringify({
            user_name: "ha_user",
            tag_id: switchData.name,
            signal_type: "switch",
            required_value: "1",
            current_value: "0",
            mode:null
        }));*/
        $http.put(url, {
            user_name:"ha_user",
            tag_id:switchData.name,
            signal_type:"switch",
            current_value:"0",
            required_value: switchData.isOn ? "1": "0",
            mode:"null"
        });
    }

    $scope.thermoModeChange = function(){
        var temp  = $scope.thermostat.temp*2;

        $http.put(url, {
            user_name:"ha_user",
            tag_id:$scope.thermostat.name,
            signal_type:"thermo",
            current_value:"0",
            required_value: temp.toString(16),
            mode: $scope.thermostat.isHeating ? "hot": "cold",
        });
    }

    var timeoutId = null;
    $scope.thermoTempChange = function(){
        if(timeoutId !== null) {
            return;
        }
        timeoutId = $timeout( function() {
            $timeout.cancel(timeoutId);
            timeoutId = null;
            var temp  = $scope.thermostat.temp*2;
            $http.put(url, {
                user_name:"ha_user",
                tag_id:$scope.thermostat.name,
                signal_type:"thermo",
                current_value:"0",
                required_value: temp.toString(16),
                mode: $scope.thermostat.isHeating ? "hot": "cold",
            });
        }, 2000); 

    }
});