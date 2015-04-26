angular.module('starter.controllers')
.controller('CoachCtrl', function ($scope, Resources) {

  $scope.resources = {};
  Resources.query({}, function( resources ) {
      $scope.resources = resources;
      console.log(resources);
  });
  $scope.speech = { currentText: "", listening: false };
  $scope.recognition = new webkitSpeechRecognition();
  $scope.recognition.continuous = true;
  $scope.recognition.interimResults = true;


  $scope.recognition.onresult = function(event) {
    console.log(event.results[0][0].transcript);
    $scope.updateSpeech({ currentText: event.results[0][0].transcript })

    if ($scope.speech.currentText === "set up treatment"){
       window.location = "#/tab/coach/1" ;
       $scope.recognition.stop();
       $scope.speech.currentText = "";
    }
  }

  $scope.speechButtonClicked = function(){
      if ($scope.speech.listening === true){
          $scope.recognition.stop();
          $scope.speech.listening = false;
      } else {
          $scope.speech.listening = true;
          $scope.recognition.start();
      }
  }

  $scope.updateSpeech = function(speechObj){
      console.log("Updating speech", speechObj)
      $scope.speech = angular.copy(speechObj);
      $scope.$apply();
      console.log($scope.speech);
  }

})

.controller('CoachDetailCtrl', function ($scope, $stateParams, $ionicSlideBoxDelegate, Resources) {
  $scope.resource = Resources.get( {id: $stateParams.resourceId} );
})

