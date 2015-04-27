angular.module('starter.controllers')
.controller('CoachCtrl', function ($scope, $interval, Resources) {

  $scope.resources = {};
  Resources.query({}, function( resources ) {
      $scope.resources = resources;
      $scope.filteredResults = resources;
      console.log(resources);
  });
  $scope.speech = { currentText: "", listening: false };
  $scope.recognition = new webkitSpeechRecognition();
  $scope.recognition.continuous = false;
  $scope.recognition.interimResults = true;


  $scope.recognition.onresult = function(event) {
    $scope.filteredResults = $scope.resources;
    console.log("On Result " + event.results[0][0].transcript);
    $scope.updateSpeech({ currentText: event.results[0][0].transcript });

    if ($scope.speech.currentText === "set up treatment"){
       window.location = "#/tab/coach/1" ;
       $scope.recognition.stop();
       $scope.speech.currentText = "";
    }
  }

  $scope.speechButtonClicked = function(){
      console.log( " Beginnign of the function ");
      if ($scope.speech.listening === true){
          console.log( "Speech recognition is true");
          $scope.recognition.stop();
          $scope.speech.listening = false;
          // Add another 3 seconds

      } else {
          console.log( "Speech recognition is false");
          $scope.speech.listening = true;
          $scope.recognition.start();
      }
  }

  $scope.updateSpeech = function(speechObj){
        results = []
        angular.forEach(speechObj.currentText.split(' '), function(value) {
          angular.forEach( $scope.resources, function ( resource ){
            for( var i = 0; i < resource.tags.length; i++ ){
              if( resource.tags[i].toLowerCase() === value){
                console.log( "Resource Found : " + resource );
                results.push( resource );
              }
            }
          });
        });

        $scope.filteredResults = results;
        $scope.speech = angular.copy(speechObj);
        $scope.$apply();
  }

})

.controller('CoachDetailCtrl', function ($scope, $stateParams, $ionicSlideBoxDelegate, Resources) {
  $scope.setAlarmCode = function (){
    var ele = document.getElementById("hdDiagram").getSVGDocument().getElementById("alarmCode");
    ele.innerHTML = $scope.resource.data.code;
  }
  $scope.resource = Resources.get( {id: $stateParams.resourceId}, function (res){
    setTimeout($scope.setAlarmCode, 100);
  });

})

