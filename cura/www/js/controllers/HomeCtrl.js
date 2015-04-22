angular.module('starter.controllers')
.controller('HomeCtrl', function ($scope, $http, $timeout) {

  var url = "http://128.2.83.208:8006/api/v1/homeautomation/ha_user/";
  // init
  $http.get(url).success(function(data){
    //update settings with data
  });

  $scope.settings = {
    tvSwitch: true,
    isHeating: true,
    temprature: 70,
    mode: function(){
      return $scope.settings.isHeating ? "Heating" : "Cooling";
    }
  };


  // TV Swtich, 1155B6
  $scope.$watch('settings.tvSwitch', function() {
    console.log('TV changed:' + $scope.settings.tvSwitch);
    $http.put(url, JSON.stringify({
      user_name: "ha_user",
      tag_id: "1155B6",
      signal_type: "swtich",
      current_value: 0,
      required_value: $scope.settings.tvSwitch ? 0 : 1
    }))
  });

  //temprature
  var timeoutId = null;
  $scope.$watch('settings.temprature', function() {
    //console.log('Has changed');
        if(timeoutId !== null) {
            //console.log('Ignoring this movement');
            return;
        }
        //console.log('Not going to ignore this one');
        timeoutId = $timeout( function() {
            console.log('It changed recently!');
            $timeout.cancel(timeoutId);
            timeoutId = null;
            // Now load data from server, check url and params
            url = "/api/v1/home_automation";
            data = {
              user_name: 'ha_user',
              tag_id: '111',
              current_value: 0,
              required_value: 1
          }
            //$http.put(url, JSON.stringify(data));
        }, 1000); 
  });

})


