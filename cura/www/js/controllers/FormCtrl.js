angular.module('starter.controllers')
.controller('FormCtrl', function ($scope, $rootScope, $ionicSlideBoxDelegate, Forms) {
  
  $scope.form = {};
  $scope.slideHasChanged = function (index){
    console.log("Slide Changed", index);
  }

  $scope.submitForm = function(){
    $rootScope.user.info = $scope.form;
    console.log($rootScope.user);
    $rootScope.user.$save(function(){
      $scope.closeModal();
    })
  }

  $scope.isPatient = function(){
    if ($scope.form.role && $scope.form.role === "patient" ){
      return true;
    } else {
      return false;
    } 
  }
  
})
