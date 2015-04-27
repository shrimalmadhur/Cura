angular.module('starter.controllers')
.controller('DashCtrl', function ($scope, $timeout, $rootScope, $ionicPlatform, $ionicModal, $ionicPopup, $cordovaVibration, $location, Forms, Events, Medications, Biometrics ) {
  

  $scope.user = $rootScope.user;

  console.log($scope.user);

  $ionicModal.fromTemplateUrl('templates/welcome-modal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.welcomeModal = modal;
    $scope.showWelcome();
  }) 

  $ionicModal.fromTemplateUrl('templates/dialysis-modal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.dialysisModal = modal
  }) 

  $ionicModal.fromTemplateUrl('templates/event-modal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.eventModal = modal
  }) 


  $scope.timeLine = [];
  $scope.events = [];

  $scope.randomOffset = function(base, offset ){
    var p = Math.random();
    if (p > 0.5){
      return (base + Math.round((Math.random() * offset)));
    } else {
      return (base - Math.round((Math.random() * offset)));
    }
  }


  $scope.duringDialysisForm = {};
  $scope.postDialysisForm = {};
  
  $scope.setPreDialysisForm = function (dialysisEventId){
    $scope.preDialysisForm = {
      bp: {systolic: $scope.randomOffset(118, 5), diastolic: $scope.randomOffset(80, 4)},
      weight: 80,
      heartRate: $scope.randomOffset(70, 5),
      dialysisEvent: dialysisEventId
    };
  }



  $scope.setPreDialysisForm();

  $scope.submitPreDialysis = function(){
    console.log("SUBMIT THIS", $scope.preDialysisForm);
    var newForm = new Forms({
      user: $scope.user._id,
      filledBy: $scope.user._id,
      type: "Pre Dialysis",
      data: $scope.preDialysisForm
    });

    var f = newForm.toJSON();

    var d = new Date()
    var formFilledEvent = new Events({
      eventType: "form",
      time: d,
      createdBy: $scope.user._id,
      createdFor: $scope.user._id,
      reminder: false,
      data: f
    })

    newForm.$save(function (res){
      console.log("SAVED THE FORM", res);
      formFilledEvent.$save(function (form){
        console.log("Form event saved", form)
        $scope.setTimeline();
        $scope.closeModal();
      })
    });

    Events.query({id: $scope.preDialysisForm.dialysisEventId}, function (res){
      var e = res[0];
      console.log("Got event!", e);
      e.data = { preFormComplete: true };
      e.$save(function(){
        $scope.setTimeline();
      })
    })

  }

  $scope.updateEvents = function(){
    $scope.events = Events.query({ createdFor: $scope.user._id});
  }

  $scope.dialysisStep = function(event){
    if (!event.data || !event.data.preFormComplete){
      return 'preForm';
    } else if (event.data && event.data.preFormComplete && !event.data.sessionFormComplete){
      return 'sessionForm';
    } else if (event.data && event.data.preFormComplete && event.data.sessionFormComplete && !event.data.postFormComplete){
      return 'postForm';
    } else {
      return 'complete';
    }
  }

  $scope.resetNewEvent = function(){
    var c1 = new Date();
    var c2 = new Date();
    $scope.newEvent = {
      createdFor: $scope.user._id,
      createdBy: $scope.user._id,
      date: c1,
      time: c2
    };    
  }

  $scope.resetNewEvent();

  $scope.setTimeline = function(){
    $scope.events = Events.query({ createdFor: $scope.user._id}, function (res){
      $scope.timeLine = res.reverse();
    });
  }

  $scope.setTimeline();


  $scope.openEventModal = function(){
    $scope.modal = $scope.eventModal;
    $scope.openModal(); 
  }

  $scope.doRefresh = function() {
    setTimeout(function(){
      $scope.setTimeline();
      $scope.$broadcast('scroll.refreshComplete');
    },1000);
  };



  $scope.getDateString = function(event){

    var date = new Date(event.time);
    return date.toLocaleTimeString({hour: '2-digit', minute:'2-digit'});
  }

  $scope.openPreDialysisModal = function(dialysisEventId){
    $scope.modal = $scope.dialysisModal;
    $scope.setPreDialysisForm(dialysisEventId);    
    $scope.openModal();
  }

  $scope.showWelcome = function(){
    if ($rootScope.user.info === undefined){
      $scope.modal = $scope.welcomeModal;
      $scope.openModal();
    }
  }

  $scope.openModal = function() {
    $scope.modal.show()
  }

  $scope.closeModal = function() {
    $scope.modal.hide();
  };

  $scope.$on('$destroy', function() {
    $scope.modal.remove();
  });


  $scope.showContactsPopup = function() {
    $scope.selectedContacts = {};

    // An elaborate, custom popup
    var myPopup = $ionicPopup.show({
      templateUrl: 'templates/contact-popup.html',
      title: 'Invite Contacts',
      subTitle: 'Add contacts ',
      scope: $scope,
      buttons: [
        { text: 'Cancel' },
        {
          text: '<b>Invite</b>',
          type: 'button-positive',
          onTap: function(e) {
            var contacts = [];
            console.log($scope.selectedContacts);
            for (var idx in $scope.selectedContacts){
              if ($scope.selectedContacts[idx] === true){
                var contact = $scope.user.contacts[idx];
                contacts.push(contact);
              }
            }
            $scope.newEvent.invited = contacts;
            return $scope.newEvent.invited
          }
        }
      ]
    });

    myPopup.then(function (res) {
      console.log('Tapped!', res);
      $scope.newEvent.invited = res;
    });
  };

  $scope.createEvent = function(){
    console.log("Creating a new event", $scope.newEvent);
    var d = $scope.newEvent.date;
    var t = $scope.newEvent.time;
    var newDate = new Date(d.getFullYear(), d.getMonth(), d.getDate(), t.getHours(), t.getMinutes());

    $scope.newEvent.time = newDate;
    delete $scope.newEvent["date"];
    console.log($scope.newEvent);

    var newEvent = new Events($scope.newEvent);
    newEvent.$save(function (res){
      console.log("event saved", res);
      $scope.resetNewEvent();
      $scope.setTimeline();
      $scope.closeModal();
    })
    // $scope.newEvent.date.setHours($scope.newEvent.date.getHours())
    // $scope.newEvent.date.setMinutes($scope.newEvent.time.getMinutes())
    // console.log("DATE", (typeof $scope.date));
  }


  
})
