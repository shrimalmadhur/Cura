# Cura

Cura is a web and mobile platform to improve patient care for both patients, caregivers and their families.

#In this repository
  - Cura front web and mobile front end
  - Cura API server
  - Dependencies and Installation
  - Troubleshooting

### Version
0.0.1

### Dependencies

To build and run this project, there are a number of dependencies that you need to have working.

* [node.js] - Javascript platform for building applications
* [ionic] - Cross platform hybrid mobile app framework
* [Django] - Python web framework
*
In order to test on a mobile device instead of a simulator, you must also ensure you have the corect compilation tools installed for your platform (iOS / Android) and code signing permissions.

### Technologies

To edit this project, you should be familiar with the following:
* Javascript, Python, HTML, CSS
* [iOS SDK] - awesome web-based text editor
* [Android SDK] - awesome web-based text editor
* [ionic] - awesome web-based text editor
 * [angular.js] - awesome web-based text editor
 * [cordova] - awesome web-based text editor
* [Django] - awesome web-based text editor

### Installation

You will need to have [node.js] and npm installed. Use the node package manager ito install  [cordova] and [ionic] globally.

```sh
$ npm install -g cordova ionic
```
Ensure you set up your keys with Github and have access to the repository. Browse to your working directory and clone the repo.
```sh
$ git clone git@github.com:shrimalmadhur/Cura.git
$ cd Cura/cura
$ ls
cura  server  .  ..
```
The /cura directory contains the ionic project for the application. To test the front end on your web browser run
```sh
$ ionic serve
```
You can also emulate the app on a device emulator or run it on your device itself.
```sh
$ ionic emulate ios
$ ionic emulate android
```
Will open the iOS emulator and android emulatos and run the application.
```sh
$ ionic run <platform>
```
Will run the application on your selected platform. To see a list of everything you an do with ionic, just type
```sh
$ ionic
```
### Server

The API server uses [Django]. It will commuincate with the platform infrastructure to fetch data to populate the frontend. This data will be accessible through an REST API.


[ionic]:http://ionicframework.com/docs/guide/installation.html
[node.js]:http://nodejs.org
[Django]:https://www.djangoproject.com
[iOS SDK]:https://developer.apple.com/devcenter/ios/index.action
[Android SDK]:http://developer.android.com/sdk/index.html
[angular.js]:http://angularjs.org
[cordova]:http://cordova.apache.org
