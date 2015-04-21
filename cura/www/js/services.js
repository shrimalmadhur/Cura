angular.module('starter.services', ['ngResource'])


.factory('Forms', function ($resource) {
  return $resource('/api/v1/Forms/:id');
})

.factory('Resources', function ($resource) {
  return $resource('/api/v1/Resources/:id');
})

.factory("Medication", function ($resource){
  return $resource('/api/v1/Medications/:id', { id: '@_id'});
})

.factory('Friends', function() {
  var friends = [];
  return {
    all: function() {
      return friends;
    },
    get: function(friendId) {
      // Simple index lookup
      return friends[friendId];
    }
  }
});
