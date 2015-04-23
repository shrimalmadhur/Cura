angular.module('starter.controllers')
.controller('MedicationsCtrl', function ($scope, $rootScope, $state, $stateParams, $ionicModal, $ionicLoading, $cordovaLocalNotification, Medications, FDA) {
  
  if ($rootScope.user === undefined){
    $state.go("account");
  }

  $scope.updateMedications = function(){
    Medications.query({ patient: $rootScope.user._id }, function (res){
      $scope.medications = res;
      console.log("MY MEDS", res);
    })
  }

  $scope.resetForm = function(){
    console.log("RESET CALLED");
    
    $scope.search = {query: "", limit: 10};
    $scope.newMedication = undefined;
    $scope.searchResults = [];
    $scope.newMedicationSchedule = {
      notifications: true,
      scheduled: true,
      frequency: "1"
    }
  }

  $scope.cancelForm = function(){
    $scope.resetForm();
    $scope.closeModal();
  }

  $scope.resetForm();
  $scope.updateMedications();


  $ionicModal.fromTemplateUrl('templates/medication-add-modal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.modal = modal
  })
  
  $scope.setScheduled = function(scheduled){
    $scope.newMedicationSchedule.scheduled = scheduled;
    console.log($scope.newMedicationSchedule.scheduled);
  }



  $scope.searchButtonClicked = function(){
    console.log("SEARCH QUERY", $scope.search.query);
    FDA.query({ search: $scope.search.query, limit: $scope.search.limit}, function (response){
      $scope.searchResults = response.results;
      console.log(response);
    })
  }

  $scope.searchResultSelected = function(i){
    console.log("A medication was selected", i, $scope.searchResults[i])
    $scope.newMedication = $scope.searchResults[i];
  }

  $scope.hasSearchResults = function(){
    if ($scope.searchResults.length > 0){
      return true;
    } else {
      return false;
    }
  }

  $scope.newMedicationSelected = function(){
    return !($scope.newMedication === undefined);
  }

  $scope.addNotification = function() {

    // var alarmTime = new Date();
    var alarmTime = $scope.newMedication.time;
    var message = $scope.newMedication.drugName + " " + $scope.newMedication.instructions;
    alarmTime.setMinutes(alarmTime.getMinutes() + 1);
     $cordovaLocalNotification.add({
           id: "1",
           date: alarmTime,
           message: message,
           title: "Medication Reminder",
           autoCancel: true,
           sound: null
      }).then(function () {
            console.log("The notification has been set");
    });
  };

  $scope.openModal = function() {
    //$scope.newMedication = new Medication();
    // $scope.newMedication.frequency = "Daily";
    $scope.modal.show();
  }

  $scope.closeModal = function() {
    $scope.modal.hide();
  };


  $scope.saveNewMedication = function() {
    if ($rootScope.user === undefined){
      $state.go("account");
    }

    var patientId = $rootScope.user._id;
    var createdBy = $rootScope.user._id;

    var newMed = new Medications({
      patient: patientId,
      createdBy: createdBy,
      instructions: $scope.newMedication.instructions,
      schedule: $scope.newMedicationSchedule,
      drugDetails: $scope.newMedication
    });

    $ionicLoading.show({
      template: "Saving Medication"
    })

    newMed.$save(function (res){
      console.log("SAVED SUCCESSFULLY", res);
      $scope.updateMedications();
      $scope.cancelForm();
      $ionicLoading.hide();
    }, function (res){
      $ionicLoading.show({
        template: "There was an error"
      })
      setTimeout(function(){ $ionicLoading.hide() }, 1000)
    });

    console.log(newMed);
        

    // $scope.newMedication.time = $scope.date;
    // $scope.newMedication.$save();
    // $scope.addNotification();
    // $scope.closeModal();
    // $scope.updateMedications();
  };

  $scope.reset = function() {
    $scope.user = angular.copy({});
  };

  $scope.updateMedications = function(){
    console.log("UPDATING MEDICATIONS");
    var patientId = $rootScope.user._id;
    Medications.query({patient: patientId}, function (res){
      $scope.medications = res;
      $scope.$apply();
    });
  }

  $scope.$on('$destroy', function() {
    $scope.modal.remove();
  });

})

.controller('MedicationDetailCtrl', function ($scope, $stateParams, Medications) {
  $scope.medication = {};
  Medications.query({_id: $stateParams.medicationId}, function (res){
    $scope.medication = res[0];
    console.log("CURRENT MED", $scope.medication);
  });
  //$scope.medication = Medications.get({id: $stateParams.medicationId});
})


