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
  //return $resource('/api/v1/Forms/:id');
  return {
    all: function(){
      return [{
        name: "Welcome",
        description: "Tell us a little about yourself",
        steps:[
          { 
            name: "Basic Information",
            fields: [
              { label: "Name",name: "name", type: "text", required: true, placeholder: "John Doe", autoPopulate: false },
              { label: "Number",name: "phone", type: "tel", required: true, placeholder: "(412) 111-3456", autoPopulate: false },
              { label: "I am a...", name: "role", type: "radio", required: true, placeholder: "John Doe", autoPopulate: false, 
                options: [
                  { label: "Patient", value: "patient", isDefault: true}, 
                  { label: "Family", value: "family"},
                  { label: "Caregiver", value: "caregiver"},
                  { label: "Doctor", value: "doctor"}
                ]}
              }
            ]
          },

          { 
            name: "Medical Information",
            fields: [
              { label: "Blood Type", name: "", type: "radio", required: true, placeholder: "John Doe", autoPopulate: false, 
                options: [
                  { label: "Patient", value: "patient", isDefault: true}, 
                  { label: "Family", value: "family"},
                  { label: "Caregiver", value: "caregiver"},
                  { label: "Doctor", value: "doctor"}
                ]}
              }
            ]
          }


        ]
      }];
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
