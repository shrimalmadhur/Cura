angular.module('starter.services', ['ngResource'])


.factory('Forms', function ($resource) {
  //return $resource('/api/v1/Forms/:id');
  return {
    all: function(){
      return [];
    }
  }
})

.factory('Resources', function ($resource) {
  // return $resource('/api/v1/Resources/:id');
  return {
    all: function(){
      return [];
    }
  }
})

.factory("Medications", function ($resource){
  //return $resource('/api/v1/Medications/:id', { id: '@_id'});
  return {
    all: function(){
      return [];
    }
  }
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
  /*var data = [];
  for (var i = 0; i < 100; i++) {
                data.push({x: i, y: Math.sin(i/10)});   
             }*/
  //console.log($resource('http://128.2.109.230:4001/sleep'));
  //http://128.2.109.230:4001/:attr/:sd/:ed
  console.log("called");
  return $resource('http://128.2.83.208:9000/api/v1/:attr/:sd/:ed',{callback: 'JSON_CALLBACK'},{
    'query': 
    {
        method:'JSONP', 
        params:{}, 
        isArray:true
    },
    'bp': 
    {
        method:'JSONP', 
        params:{}, 
        isArray:true
    }
  })
});
