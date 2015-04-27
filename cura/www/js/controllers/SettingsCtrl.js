angular.module('starter.controllers')
.controller('SettingsCtrl', function ($scope, $rootScope, $stateParams) {
   $scope.user = $rootScope.user;
   $scope.getDateString = function(dateStr){
   	var d = new Date(dateStr);
   	var str = d.toDateString();
   	return str;
   }
})


