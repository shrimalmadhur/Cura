angular.module('starter.controllers', ['ngCordova'])
 
.controller('AppCtrl', function ($scope, $ionicPlatform, $ionicModal, $http, $ionicLoading, $rootScope){
  $scope.registrationForm = {};
  $scope.loginForm = {};

  $scope.login = function(){

    $ionicLoading.show({
      template: "Loading"
    })
    
    $http.post('/login', $scope.loginForm).
    success(function(data, status, headers, config) {
      $rootScope.user = data;

      setTimeout(function(){
        window.location = "#/tab/dash";
        $ionicLoading.hide();
      }, 1500)
    }).
    error(function(data, status, headers, config) {
      setTimeout(function(){
        $ionicLoading.hide();
      }, 1500)
    });
  }


  $scope.register = function(){
    $ionicLoading.show({
      template: "Loading"
    })

    $http.post('/register', $scope.registrationForm).
    success(function(data, status, headers, config) {
      $rootScope.user = data;

      setTimeout(function(){
        window.location = "#/login";
        $ionicLoading.hide();
      }, 1500)
    }).
    error(function(data, status, headers, config) {
      setTimeout(function(){
        $ionicLoading.hide();
      }, 1500)
    });
  }
})


.controller('DashCtrl', function($scope, $ionicPlatform, $ionicModal, $cordovaVibration, $location, Forms) {
  $scope.alarmInterval = undefined;
  $scope.forms = Forms.all();
  $scope.currentForm = $scope.forms[0];
  
  $ionicModal.fromTemplateUrl('templates/form-fill-modal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.modal = modal
  }) 


  $scope.openModal = function() {
    $scope.modal.show()
  }

  $scope.closeModal = function() {
    $scope.modal.hide();
  };

  $scope.$on('$destroy', function() {
    $scope.modal.remove();
  });

  $scope.doAlarm = function(){
      $scope.alarmInterval = setInterval(function(){ 
        $cordovaVibration.vibrate(100) 
      }, 1000);
      $scope.openModal();
  }

  $scope.stopAlarm = function(){
    $scope.closeModal();
    clearInterval($scope.alarmInterval);
  }
})

.controller('CoachCtrl', function($scope, Resources) {
  $scope.resources = Resources.all();
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

.controller('CoachDetailCtrl', function($scope, $stateParams, $ionicSlideBoxDelegate, Resources) {
  $scope.resource = Resources.get($stateParams.resourceId);

})


.controller('ChatsCtrl', function($scope, Chats) {
  $scope.chats = Chats.all();

  $scope.remove = function(chat) {
    Chats.remove(chat);
  }
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('SettingsCtrl', function($scope, $stateParams) {
  //$scope.chat = Chats.get($stateParams.chatId);
})

.controller('FriendsCtrl', function($scope, $cordovaContacts, Friends) {
  $scope.friends = Friends.all();
  $scope.addContact = function(){
    $cordovaContacts.pickContact().then(function (contact){
      alert(JSON.stringify(contact))      
      $scope.friends.push(contact);
    })
  }
})

.controller('FriendDetailCtrl', function($scope, $stateParams, Friends) {
  $scope.friend = Friends.get($stateParams.friendId);
})

.controller('MedicationsCtrl', function($scope, $stateParams, $ionicModal, $cordovaLocalNotification, Medications){
  
  $scope.medications = Medications.all();
  $ionicModal.fromTemplateUrl('templates/medication-add-modal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.modal = modal
  })  
  $scope.newMedication = {};


  $scope.openModal = function() {
    $scope.modal.show()
  }

  $scope.closeModal = function() {
    $scope.modal.hide();
  };

  $scope.$on('$destroy', function() {
    $scope.modal.remove();
  });

  $scope.update = function(newMedication) {
    var newId = $scope.medications.length;
    var newMed = angular.copy(newMedication);
    newMed.id = newId;
    $scope.medications.push(newMed);
    $scope.closeModal()

    var alarmTime = new Date();
    alarmTime.setSeconds(alarmTime.getSeconds() + 10);
    Medications.sync($scope.medications);
    console.log(Medications.all())
  };

  $scope.reset = function() {
    $scope.user = angular.copy({});
  };




})

.controller('MedicationDetailCtrl', function($scope, $stateParams, Medications) {

  $scope.medication = {};
  console.log("DETAIL CTRL");
  $scope.medication = Medications.get($stateParams.medicationId);
  console.log(Medications.all())
})

.controller('HomeCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
})
.controller('DemoCtrl', function($scope, $stateParams) {
  //$scope.chat = Chats.get($stateParams.chatId);
  $scope.options = [
    { label: 'one', value: 1 },
    { label: 'two', value: 2 },
    { label: 'three', value: 3 },
    { label: 'four', value: 4 },
    { label: 'five', value: 5 }
  ];
    
  // Although this object has the same properties as the one in $scope.options,
  // Angular considers them different because it compares based on reference
  $scope.incorrectlySelected = { label: 'two', value: 2 };
    
  // Here we are referencing the same object, so Angular inits the select box correctly
  $scope.correctlySelected = $scope.options[1];
});

