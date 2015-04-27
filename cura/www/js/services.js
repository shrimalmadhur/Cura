angular.module('starter.services', ['ngResource'])

.factory('FDA', function ($resource){
  return $resource('https://api.fda.gov/drug/label.json', {}, {
    'query': {isArray: false}
  });
})

.factory('Config', function (){
  
  var host = "";
  //var host = "http://rpcs.herokuapp.com";
  var apiUrl = host + "/api/v1/";
  var loginEndpoint = host + "/login";
  var registerEndpoint = host + "/register";

  return {
    host: host,
    apiUrl: apiUrl,
    loginEndpoint: loginEndpoint,
    registerEndpoint: registerEndpoint
  }
})

.factory('Forms', function ($resource) {
  return $resource('/api/v1/Forms/:id'); 
})

.factory('Events', function ($resource, Config) {
  var url = Config.apiUrl + "Events/:id";
  return $resource(url, {id: "@_id"}); 
})

.factory('Biometrics', function ($resource) {
  return $resource('/api/v1/Biometrics/:id'); 
})

.factory('Resources', function ($resource, Config) {
  return $resource('/api/v1/Resources/:id', { id: '@_id'});
})

.factory("Users", function ($resource, Config){
  var url = Config.apiUrl + "Users/:id"
  return $resource(url, { id: "@_id"});
})

.factory("Medications", function ($resource, Config){
  var url = Config.apiUrl + "Medications/:id"
  return $resource(url, { id: '@_id'});
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
})

.factory('Stress', function() {
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
})

.factory('Visuals', function($resource) {
  return $resource('http://128.2.83.208:8001/api/v1/:attr/mshrimal/:sd/:ed')
});
