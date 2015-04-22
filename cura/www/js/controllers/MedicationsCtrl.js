angular.module('starter.controllers')
.controller('MedicationsCtrl', function ($scope, $stateParams, $ionicModal, $cordovaLocalNotification, Medications) {
  $scope.medications = Medications.all();

  $ionicModal.fromTemplateUrl('templates/medication-add-modal.html', {
    scope: $scope,
    animation: 'slide-in-up'
  }).then(function(modal) {
    $scope.modal = modal
  })  

  $scope.newMedication = undefined;

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
    $scope.newMedication = new Medication();
    $scope.newMedication.frequency = "Daily";
    $scope.modal.show();
  }

  $scope.closeModal = function() {
    $scope.modal.hide();
  };


  $scope.saveNewMed = function() {
    console.log("SAVING")
    $scope.newMedication.time = $scope.date;
    $scope.newMedication.$save();
    $scope.addNotification();
    $scope.closeModal();
    $scope.updateMedications();
  };

  $scope.reset = function() {
    $scope.user = angular.copy({});
  };

  $scope.updateMedications = function(){
    console.log("UPDATING MEDICATIONS");
    $scope.newMedication.time = $scope.date;
    $scope.addNotification();
    $scope.medications = Medication.query(function(){
      console.log($scope.medications);
      $scope.$apply();
    });
  }

  $scope.$on('$destroy', function() {
    $scope.modal.remove();
  });

})

.controller('MedicationDetailCtrl', function ($scope, $stateParams, Medication) {
  $scope.medication = {};
  $scope.medication = Medication.get({id: $stateParams.medicationId});
})


