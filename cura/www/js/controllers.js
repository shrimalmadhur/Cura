angular.module('starter.controllers', ['ngCordova','nvd3'])

.controller('DashCtrl', function($scope, $ionicPlatform, $ionicModal, $cordovaVibration) {
  $scope.alarmInterval = undefined;

  $ionicModal.fromTemplateUrl('contact-modal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.modal = modal
  })  


  $scope.openModal = function() {
    $scope.modal.show()
  }

  $scope.closeModal = function() {
    $scope.modal.hide();
  };

  $scope.$on('$destroy', function() {
    $scope.modal.remove();
  });

  $scope.doAlarm = function(){
      $scope.alarmInterval = setInterval(function(){ 
        $cordovaVibration.vibrate(100) 
      }, 1000);

      $scope.openModal();
  }

  $scope.stopAlarm = function(){
    $scope.closeModal();
    clearInterval($scope.alarmInterval);
  }
})

.controller('ChatsCtrl', function($scope, Chats) {
  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  }
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('FriendsCtrl', function($scope, $cordovaContacts, Friends) {
  $scope.friends = Friends.all();
  $scope.addContact = function(){
    $cordovaContacts.pickContact().then(function (contact){
      alert(JSON.stringify(contact))      
      $scope.friends.push(contact);
    })
  }
})

.controller('FriendDetailCtrl', function($scope, $stateParams, Friends) {
  $scope.friend = Friends.get($stateParams.friendId);
})

.controller('VisualCtrl', function($scope, $stateParams, Visuals) {
  
  $scope.items = [
            {id:0,urlName:"sleep", name:"Sleep", yAxisLabel:"Phases"},
            {id:1,urlName:"bp",name:"Blood Pressure", yAxisLabel:"bp level"},
            {id:2, urlName:"rr",name: "Respiration Rate", yAxisLabel:"rr level"},
            {id:3, urlName:"wgt",name: "Weight over time", yAxisLabel:"Lbs"},
            {id:4, urlName:"multi",name: "Heart Rate", yAxisLabel:"beats/mins"},
            {id:5, urlName:"stress",name: "Stress", yAxisLabel:"Stress Units"},
            {id:6, urlName:"skin",name: "Skin Temperature", yAxisLabel:"Degree"}
            ];
  
  //$scope.entries = Visuals.query({attr:"sleep",sd:"akshay", ed:"pushparaja"});
  
  $scope.update = function(){
    
    $scope.updateWithParams(0,0);
    /*$scope.vOption.title.text = $scope.vOption.menuSelect.name+" Chart";
    $scope.vOption.chart.yAxis.axisLabel = $scope.vOption.menuSelect.yAxisLabel;

    var colorOptions = ["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b","#e377c2","#7f7f7f","#bcbd22","#17becf"];
    $scope.visuals = [];

    $scope.visuals = Visuals.bp({attr:$scope.vOption.menuSelect.urlName,sd:"2013-01-29T00:00:00.000000Z", ed:"2013-01-30T00:00:00.000000Z"}, function(){  
      for (var i = 0; i < $scope.visuals.length; i++) {
        $scope.visuals[i]["color"] = colorOptions[i];
      };
    });*/ 
  }
  
  $scope.updateWithParams = function(sd,ed){
    
    $scope.sleepDisplay = false;
    
    if ($scope.vOption.menuSelect.id == 0) {
      $scope.sleepDisplay = true;
    }
    $scope.vOption.title.text = $scope.vOption.menuSelect.name+" Chart";
    $scope.vOption.chart.yAxis.axisLabel = $scope.vOption.menuSelect.yAxisLabel;

    var colorOptions = ["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b","#e377c2","#7f7f7f","#bcbd22","#17becf"];
    $scope.visuals = [];

    $scope.visuals = Visuals.bp({attr:$scope.vOption.menuSelect.urlName,sd:"2013-01-29T00:00:00.000000Z", ed:"2013-01-30T00:00:00.000000Z"}, function(){  
      for (var i = 0; i < $scope.visuals.length; i++) {
        $scope.visuals[i]["color"] = colorOptions[i];
      };
    }); 
  }

  $scope.day = function(){
    var fd = new Date();
    var y = fd.getFullYear();
    var m = fd.getMonth();
    var d = fd.getDate();
    var currentDay = y+"-"+m+"-"+d+"T00:00:00.000000Z";
    var nd = new Date();
    nd.setDate(d+10);
    var nextDay = y+"-"+m+"-"+nd.getDate()+"T00:00:00.000000Z";
    console.log(currentDay+"  "+nextDay);
  }
  
  $scope.week = function(){
    console.log("week"); 
  }

  $scope.month = function(){
    console.log("month");
  }

  $scope.next = function(){
    console.log("next");
  }

  $scope.prev = function(){
    console.log("prev");
  }

  $scope.visuals = [{values:$scope.entries, key:'Test Wave', color: '#ff7f0e'}];
  $scope.vOption = {
            chart: {
                type: 'lineChart',
                height: 450,
                margin : {
                    top: 20,
                    right: 20,
                    bottom: 40,
                    left: 55
                },
                x: function(d){ return d.x; },
                y: function(d){ return d.y; },
                useInteractiveGuideline: true,
                dispatch: {
                    /*stateChange: function(e){ console.log("stateChange"); },
                    changeState: function(e){ console.log("changeState"); },
                    tooltipShow: function(e){ console.log("tooltipShow"); },
                    tooltipHide: function(e){ console.log("tooltipHide"); }*/
                },
                xAxis: {
                    axisLabel: 'Time (ms)'
                },
                yAxis: {
                    axisLabel: 'Voltage (v)',
                    tickFormat: function(d){
                        return d3.format('.02f')(d);
                    },
                    axisLabelDistance: 30
                },
                callback: function(chart){
                    console.log("!!! lineChart callback !!!");              
                }
            },
            period:{ value: new Date()},
            title: {
                enable: false,
                text: 'Line Chart Sample 1'
            }/*,
            subtitle: {
                enable: true,
                text: 'Subtitle for simple line chart. Lorem ipsum dolor sit amet, at eam blandit sadipscing, vim adhuc sanctus disputando ex, cu usu affert alienum urbanitas.',
                css: {
                    'text-align': 'center',
                    'margin': '10px 13px 0px 7px'
                }
            },
            caption: {
                enable: true,
                html: '<b>Figure 1.</b> Lorem ipsum dolor sit amet, at eam blandit sadipscing, <span style="text-decoration: underline;">vim adhuc sanctus disputando ex</span>, cu usu affert alienum urbanitas. <i>Cum in purto erat, mea ne nominavi persecuti reformidans.</i> Docendi blandit abhorreant ea has, minim tantas alterum pro eu. <span style="color: darkred;">Exerci graeci ad vix, elit tacimates ea duo</span>. Id mel eruditi fuisset. Stet vidit patrioque in pro, eum ex veri verterem abhorreant, id unum oportere intellegam nec<sup>',
                css: {
                    'text-align': 'justify',
                    'margin': '10px 13px 0px 7px'
                }
            }*/
        };
        
        $scope.vOption.menuSelect = $scope.items[0];
        $scope.update();
})

.controller('MedicationsCtrl', function($scope, $stateParams, $ionicModal, $cordovaLocalNotification, Medications){
  $scope.medications = Medications.all();

  $ionicModal.fromTemplateUrl('templates/medication-add-modal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.modal = modal
  })  

  $scope.newMedication = {};


  $scope.openModal = function() {
    $scope.modal.show()
  }

  $scope.closeModal = function() {
    $scope.modal.hide();
  };

  $scope.$on('$destroy', function() {
    $scope.modal.remove();
  });

  $scope.update = function(newMedication) {

    var newId = $scope.medications.length;
    var newMed = angular.copy(newMedication);
    newMed.id = newId;
    $scope.medications.push(newMed);
    $scope.closeModal()

    console.log($scope.medications)


    var alarmTime = new Date();
    alarmTime.setSeconds(alarmTime.getSeconds() + 15);
    Medications.sync($scope.medications);
    console.log(Medications.all())
    // $cordovaLocalNotification.add({
    //     id: "1234",
    //     date: alarmTime,
    //     message: "This is a message",
    //     title: "This is a title",
    //     autoCancel: true,
    //     sound: null
    // }).then(function () {
    //     alert("The notification has been set");
    // });




  };

  $scope.reset = function() {
    $scope.user = angular.copy({});
  };




})

.controller('MedicationDetailCtrl', function($scope, $stateParams, Medications) {

  $scope.medication = {};
  console.log("DETAIL CTRL");
  $scope.medication = Medications.get($stateParams.medicationId);
  console.log(Medications.all())
})

.controller('HomeCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
});
