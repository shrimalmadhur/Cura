angular.module('starter.services', [])

.factory('Config', function(){
  var serverHostPort = "127.0.0.1:8000";
  return {
    serverHostPort: serverHostPort
  }



})


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

.factory('Forms', function() {
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var forms = [{
    id: 0,
    name: 'NxStage Short Home Hemodialysis Treatment Sheet',
    prompt: 'Pre-Treatment Form',
    description: "Please fill out the NxStage Short Home Hemodialysis Treatment Sheet. If you have any questions regarding this form, contact your caregiver.",
    fields: [
      { name: "date", type: "date"},
      { name: "cartridge lot number", type: "number"},
      { name: "chloramine test", type: "option"},
      { name: "fluid detector test/machine", type: "option"},
      { name: "pre weight", type: "number"},
      { name: "dry weight", type: "number"},
      { name: "fluid to remove", type: "number"},
      { name: "pre temperature", type: "number"},
      { name: "pre bp systolic", type3: "number"},
      { name: "pre bp diastolic", type: "number"},
      { name: "pre pulse", type: "number"},
      { name: "initial heparin dose", type: "number"},
      { name: "initial bp systolic", type: "number"},
      { name: "initial bp diastolic", type: "number"},
      { name: "initial pulse", type: "number"},
      { name: "ultrafilteration rate", type: "number"},
      { name: "venous at max BFR", type: "number"},
      { name: "effluent at max BFR", type: "number"},
      { name: "arterial at max BFR", type: "number"},
      { name: "bp systolic", type: "number"},
      { name: "bp diastolic", type: "number"},
      { name: "pulse", type: "number"},
      { name: "total treatment time", type: "number"},
      { name: "total dialysate volume", type: "number"},
      { name: "total ultrafiltration", type: "number"},
      { name: "solution infusion number", type: "number"},
      { name: "post sitting bp systolic", type: "number"},
      { name: "post sitting bp diastolic", type: "number"},
      { name: "post sitting pulse", type: "number"},
      { name: "post weight", type: "number"},
      { name: "labs drawn", type: "boolean"},
      { name: "signature", type: "text"}
    ]
  }]

  return {
    all: function() {
      return forms;
    },
    get: function(formId) {
      return forms[formId];
    }
  }
})




.factory('Resources', function() {
    var videos = [{
      id: 0,
      code: 11,
      type: "alarm",
      contact: true,
      title: "Arterial Air Detected",
      description: "Air has been detected in the arterial. Please check for an empty saline bag or embolus in the arterial cartidge.",
      url: undefined,
      steps:[{title: "Check saline bag", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."}]
    },
    {
      id: 1,
      code: 1,
      type: "tutorial",
      contact: false,
      title: "Setup for Treatment",
      description: "This video provides an overview of how to use the NxStage System One Cycler with bagged dialysate and the Express Fluid Warmer. It is not intended to replace the NxStage System One User's Guide or Cartridge Instructions for Use. Patients, partners, and providers should review and refer to the System One User's Guide and Cartridge Instructions for Use for all warnings and precautions.",
      url: "img/setup.mp4",
      steps:[
        {title: "Complete pre-treatment assessment", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Gather and inspect materials", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Prepare the warmer", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Remove and prepare the Cartridge", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Test fluid detection sensor", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Insert saline priming spike", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Attach access pressure pod", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Press ADD FLUID on the Cycler", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Prepare the Warmer disposables", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Clamp Dialysate Outlet Line", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Secure waste line extension", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Observe the Prime and Alarms Test", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Remove air from the blood circuit", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Press STOP then prime and clamp the Saline T", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."},
        {title: "Make fluid line connections", description: "Make sure that the saline bag is not empty. An empty saline bag can cause air to be introduced into the tubing system."}
      ]
    }];

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
});
