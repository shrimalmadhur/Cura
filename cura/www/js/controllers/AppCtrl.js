angular.module('starter.controllers')
.controller('AppCtrl', function ($scope, $ionicPlatform, $ionicModal, $http, $ionicLoading, $rootScope, Config) {

  $scope.registrationForm = {};
  $scope.loginForm = {};

  $scope.login = function(){

    $ionicLoading.show({
      template: "Loading"
    })

    var authEndpoint = Config.a
    
    $http.post(Config.loginEndpoint, $scope.loginForm).
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
