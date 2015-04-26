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
  $scope.newEvent = {};

  $scope.setTimeline = function(){

  }


  $scope.openEventModal = function(){
    $scope.modal = $scope.eventModal;
    $scope.openModal(); 
  }

  $scope.doRefresh = function() {
    setTimeout(function(){
      $scope.$broadcast('scroll.refreshComplete');
    },2000);
  };

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
    });

  };


  
})
