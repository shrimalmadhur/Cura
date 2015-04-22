angular.module('starter.controllers')
.controller('DashCtrl', function ($scope, $ionicPlatform, $ionicModal, $cordovaVibration, $location, Forms) {

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
