// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.services' is found in services.js
// 'starter.controllers' is found in controllers.js

angular.module('starter', ['ionic', 'starter.controllers', 'starter.services', 'ionic-timepicker', 'nvd3','angularMoment'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    if (window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
    }
    if (window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }
  });
})

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider

  .state('account', {
    url: '/login',
    templateUrl: 'templates/login.html',
    controller: 'AppCtrl'
  })
  

  .state('register', {
    url: '/register',
    templateUrl: 'templates/register.html',
    controller: 'AppCtrl'
  })
  

  .state('retrive', {
    url: '/retrive-account',
    templateUrl: 'templates/retrive-account.html',
    controller: 'AppCtrl'
  })


  // setup an abstract state for the tabs directive
  .state('tab', {
    url: "/tab",
    abstract: true,
    templateUrl: "templates/tabs.html"
  })

  // Each tab has its own nav history stack:

  .state('tab.dash', {
    url: '/dash',
    views: {
      'tab-dash': {
        templateUrl: 'templates/tab-dash.html',
        controller: 'DashCtrl'
      }
    }
  })

  .state('tab.contacts', {
      url: '/contacts',
      views: {
        'tab-contacts': {
          templateUrl: 'templates/tab-contacts.html',
          controller: 'ContactsCtrl'
        }
      }
    })
    .state('tab.contact-detail', {
      url: '/contact/:contactId',
      views: {
        'tab-contacts': {
          templateUrl: 'templates/contact-detail.html',
          controller: 'ContactDetailCtrl'
        }
      }
    })



  .state('tab.home', {
    url: '/home',
    views: {
      'tab-home': {
        templateUrl: 'templates/tab-home.html',
        controller: 'HomeCtrl'
      }
    }
  })

  // TODO: Change this to monitor
  .state('tab.visualization', {
    url: '/visual',
    views: {
      'tab-visualization': {
        templateUrl: 'templates/tab-visualization.html',
        controller: 'VisualCtrl'
      }
    }
  })

  .state('tab.medication', {
    url: '/medication',
    views: {
      'tab-medication': {
        templateUrl: 'templates/tab-medication.html',
        controller: 'MedicationsCtrl'
      }
    }
  })

  // .state('tab.stress', {
  //   url: '/stress',
  //   views: {
  //     'tab-stress': {
  //       templateUrl: 'templates/tab-stress.html',
  //       controller: 'StressCtrl'
  //     }
  //   }
  // })

  .state('tab.medication-detail', {
    url: '/medication/:medicationId',
    views: {
      'tab-medication': {
        templateUrl: 'templates/medication-detail.html',
        controller: 'MedicationDetailCtrl'
      }
    }
  })

  .state('tab.coach', {
    url: '/coach',
    views: {
      'tab-coach': {
        templateUrl: 'templates/tab-coach.html',
        controller: 'CoachCtrl'
      }
    }
  })

  .state('tab.coach-detail', {
    url: '/coach/:resourceId',
    views: {
      'tab-coach': {
        templateUrl: 'templates/coach-detail.html',
        controller: 'CoachDetailCtrl'
      }
    }
  })

  .state('tab.settings',{
    url: '/settings',
    views: {
      'tab-settings': {
        templateUrl: 'templates/tab-settings.html',
        controller: 'SettingsCtrl'
      }
    }
  })


  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/login');

})

