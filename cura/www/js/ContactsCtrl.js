angular.module('starter.controllers')
.controller('ContactsCtrl', function ($scope, $cordovaContacts, Friends) {

  $scope.friends = Friends.all();
  $scope.addContact = function(){
    $cordovaContacts.pickContact().then(function (contact){
      alert(JSON.stringify(contact))      
      $scope.friends.push(contact);
    })
  }

})

.controller('ContactDetailCtrl', function ($scope, $stateParams, Friends) {
  $scope.friend = Friends.get($stateParams.friendId);
})


