angular.module('starter.controllers')
.controller('ContactsCtrl', function ($scope, $rootScope, $stateParams, $cordovaContacts) {

    $scope.search = { query: "", limit: 1}
    $scope.contacts = $rootScope.user.contacts;

    console.log($scope.contacts);

    $scope.saveContactToUser = function(contact){
    	$rootScope.user.contacts.push(contact);
    	$rootScope.user.$save(function(){
    		alert("Updated the users contacts");
    	});
    }

    $scope.addContactClicked = function(){
    	$cordovaContacts.pickContact().then(function (contact){
    		$scope.saveContactToUser(contact);
    	});
    }

})

.controller('ContactDetailCtrl', function ($scope, $rootScope, $stateParams) {
    $scope.contact = $rootScope.user.contacts[$stateParams.contactId];
    $scope.disable = true;

    $scope.toggleEdit = function(){
    	$scope.disable = !$scope.disable;
    	console.log($scope.find("input"))
    }

})



