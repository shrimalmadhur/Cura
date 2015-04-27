angular.module('starter.controllers', [])

.controller('DashCtrl', function($scope) {})

.controller('ChatsCtrl', function($scope, Chats) {
  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  }
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('FriendsCtrl', function($scope, Friends) {
  $scope.friends = Friends.all();
})

.controller('FriendDetailCtrl', function($scope, $stateParams, Friends) {
  $scope.friend = Friends.get($stateParams.friendId);
})

.controller('StressCtrl', function($scope) {
	$scope.stress =  {question:'Had trouble keeping my mind on what I was doing... ',option1:'Yes',option2:'No',value1:'11',value2:'12'}
	$scope.stress1 = {question:'Felt that I couldn’t leave my relative alone... ',option1:'Yes',option2:'No',value1:'21',value2:'22'}
	$scope.stress2 = {question:'Had difficulty making decisions...',option1:'Yes',option2:'No',value1:'31',value2:'32'}
	$scope.stress3 = {question:'Felt completely overwhelmed...',option1:'Yes',option2:'No',value1:'41',value2:'42'}
	$scope.stress4 = {question:'Felt useful and needed...',option1:'Yes',option2:'No',value1:'51',value2:'52'}
	$scope.stress5 = {question:'Felt lonely...',option1:'Yes',option2:'No',value1:'61',value2:'62'}
	$scope.stress6 = {question:'Been upset that my relative has changed so much from his/her former self...',option1:'Yes',option2:'No',value1:'71',value2:'72'}
})

.controller('StressCtrl1', function($scope) {
	
	})
	
.controller('StressCtrl2', function($scope) {
$scope.initTabs= function(){
		$(function(){
			$("#tabs").tabs();
		});
	};
	
	$scope.initTabs();
	})


.controller('StressCtrl3', function($scope) {

	$scope.instructions=[{
   number: "1.",
   text: "Connect PIP to your android device"
  }, {
     number: "2.",
   text: "Hold the PIP between your thumb and index finger"
  }, {
      number: "3.",
   text: "Wait for 10 seconds until connection is established"
  }, {
      number: "4.",
   text: "After successful connection,proceed to next page"
  }];
	
	})


.controller('StressCtrl4', function($scope) {
		$scope.init=function(){
			$.ajax({
				url: "http://128.2.83.208:8001/api/v1/stress/recent/user_testing/?format=json",
				dataType: "json",
				success: function(response){
					$("#StressEvents").html("<h3><b>Stress Events:     </b>"+response[0]["number_stress_events"]+"</h3>");
					$("#RelaxedEvents").html("<h3><b>Relaxed Events:   </b>"+response[0]["number_relax_events"]+"</h3>");
					$("#SteadyEvents").html("<h3><b>Steady Events:   </b>"+response[0]["number_steady_events"]+"</h3>");
					$("#FinalScore").html("<h3><b>Final Score:   </b>"+response[0]["stress_score"]+"</h3>");
				},
				error:function(){
					alert("Hi.");
				}
			});
		};
		
		$scope.init();
	})
	
	.controller('StressCtrl5', function($scope) {
		$scope.initTabs= function(){
		$(function(){
			 window.setTimeout(function () {
        	 	window.location.href = "#/tab/stress/Questions/GO/discovery/wait/status";
    		}, 10000)
		});
	};
	
	$scope.initTabs();
	})




.controller('StressCtrl6', function($scope) {
		$scope.suggestions=[{
   number: "1.",
   text: "Take deep breaths"
  }, {
     number: "2.",
   text: "Eat a snack"
  }, {
      number: "3.",
   text: "Step away from the screen and go for a long walk"
  }, {
      number: "4.",
   text: "Put on your favorite music"
  }, {
     number: "5.",
   text: "Watch a funny video"
  }, {
     number: "6.",
   text: "Eat a banana"
  }, {
      number: "7.",
   text: "Call a friend"
  }, {
     number: "8.",
   text: "Chew a piece of gum"
  }, {
      number: "9.",
   text: "Eat one (ONE!) candy"
  }, {
     number: "10.",
   text: "Sing your favorite song"
  }];
	})
	
.controller('AccountCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
});
