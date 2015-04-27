angular.module('starter.controllers')
.controller('DashCtrl', function ($scope, $timeout, $rootScope, $ionicPlatform, $ionicModal, $ionicPopup, $cordovaVibration, $location, Forms, Events, Medications, Biometrics ) {
  

  $scope.user = $rootScope.user;

  console.log($scope.user);

  $ionicModal.fromTemplateUrl('templates/welcome-modal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.welcomeModal = modal;
    $scope.showWelcome();
  }) 

  $ionicModal.fromTemplateUrl('templates/dialysis-modal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.dialysisModal = modal
  }) 

  $ionicModal.fromTemplateUrl('templates/event-modal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.eventModal = modal
  }) 


  $scope.timeLine = [];
  $scope.events = [];


  $scope.updateEvents = function(){
    $scope.events = Events.query({ createdFor: $scope.user._id});
  }

  $scope.resetNewEvent = function(){
    var c1 = new Date();
    var c2 = new Date();
    $scope.newEvent = {
      createdFor: $scope.user._id,
      createdBy: $scope.user._id,
      date: c1,
      time: c2
    };    
  }

  $scope.resetNewEvent();

  $scope.setTimeline = function(){
    $scope.updateEvents();
    console.log("Events updated");
    $scope.timeLine = $scope.events;
    console.log($scope.timeLine)
  }

  $scope.setTimeline();


  $scope.openEventModal = function(){
    $scope.modal = $scope.eventModal;
    $scope.openModal(); 
  }

  $scope.doRefresh = function() {
    setTimeout(function(){
      $scope.$broadcast('scroll.refreshComplete');
    },2000);
  };

  $scope.getDateString = function(str){
    var d = new Date(str);
    var t = new date();

    // An event happening today
    // TODO: make his 
    return d.toTimeString();
  }

  $scope.showWelcome = function(){
    if ($rootScope.user.info === undefined){
      $scope.modal = $scope.welcomeModal;
      $scope.openModal();
    }
  }

  $scope.openModal = function() {
    $scope.modal.show()
  }

  $scope.closeModal = function() {
    $scope.modal.hide();
  };

  $scope.$on('$destroy', function() {
    $scope.modal.remove();
  });


  $scope.showContactsPopup = function() {
    $scope.selectedContacts = {};

    // An elaborate, custom popup
    var myPopup = $ionicPopup.show({
      templateUrl: 'templates/contact-popup.html',
      title: 'Invite Contacts',
      subTitle: 'Add contacts ',
      scope: $scope,
      buttons: [
        { text: 'Cancel' },
        {
          text: '<b>Invite</b>',
          type: 'button-positive',
          onTap: function(e) {
            var contacts = [];
            console.log($scope.selectedContacts);
            for (var idx in $scope.selectedContacts){
              if ($scope.selectedContacts[idx] === true){
                var contact = $scope.user.contacts[idx];
                contacts.push(contact);
              }
            }
            $scope.newEvent.invited = contacts;
            return $scope.newEvent.invited
          }
        }
      ]
    });

    myPopup.then(function (res) {
      console.log('Tapped!', res);
      $scope.newEvent.invited = res;
    });
  };

  $scope.createEvent = function(){
    console.log("Creating a new event", $scope.newEvent);
    var d = $scope.newEvent.date;
    var t = $scope.newEvent.time;
    var newDate = new Date(d.getFullYear(), d.getMonth(), d.getDate(), t.getHours(), t.getMinutes());

    $scope.newEvent.time = newDate;
    delete $scope.newEvent["date"];
    console.log($scope.newEvent);

    var newEvent = new Events($scope.newEvent);
    newEvent.$save(function (res){
      console.log("event saved", res);
      $scope.resetNewEvent();
      $scope.setTimeline();
      $scope.closeModal();
    })
    // $scope.newEvent.date.setHours($scope.newEvent.date.getHours())
    // $scope.newEvent.date.setMinutes($scope.newEvent.time.getMinutes())
    // console.log("DATE", (typeof $scope.date));
  }


  
})
