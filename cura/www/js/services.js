angular.module('starter.services', ['ngResource'])

.factory('Chats', function() {
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var chats = [{
    id: 0,
    name: 'Ben Sparrow',
    lastText: 'You on your way?',
    face: 'https://pbs.twimg.com/profile_images/514549811765211136/9SgAuHeY.png'
  }, {
    id: 1,
    name: 'Max Lynx',
    lastText: 'Hey, it\'s me',
    face: 'https://avatars3.githubusercontent.com/u/11214?v=3&s=460'
  }, {
    id: 2,
    name: 'Andrew Jostlin',
    lastText: 'Did you get the ice cream?',
    face: 'https://pbs.twimg.com/profile_images/491274378181488640/Tti0fFVJ.jpeg'
  }, {
    id: 3,
    name: 'Adam Bradleyson',
    lastText: 'I should buy a boat',
    face: 'https://pbs.twimg.com/profile_images/479090794058379264/84TKj_qa.jpeg'
  }, {
    id: 4,
    name: 'Perry Governor',
    lastText: 'Look at my mukluks!',
    face: 'https://pbs.twimg.com/profile_images/491995398135767040/ie2Z_V6e.jpeg'
  }];

  return {
    all: function() {
      return chats;
    },
    remove: function(chat) {
      chats.splice(chats.indexOf(chat), 1);
    },
    get: function(chatId) {
      for (var i = 0; i < chats.length; i++) {
        if (chats[i].id === parseInt(chatId)) {
          return chats[i];
        }
      }
      return null;
    }
  }
})

.factory('Resources', function() {
    var videos = [{
      id: 0,
      name: "Alarm 39",
      description: "Low blood pressure"
    }, {
      id: 1,
      name: "Alarm 11",
      description: "High Venous Blood pressure"
    }]

    return {
      all: function(){
        return videos;
      },
      get: function(resourceId){
        return videos[resourceId];
      }
    }
})

.factory("Medications", function(){
  var medications = []

  return {
    all: function(){
      return medications;
    },
    get: function(medicationId){
      return medications[medicationId];
    }, 
    sync: function(newArray){
      console.log("SYNCING")
      medications = newArray;
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
