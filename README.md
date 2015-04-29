### Cura

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
If you're developing server (Django), you'll need [virtualenv] to create virtual enviornment for python packages managed with [pip]. make sure you activate environment when developing.

```sh
$ virtualenv curaEnv
$ cd curaEnv
$ source bin/activate
(curaEnv)$ git clone git@github.com:shrimalmadhur/Cura.git
(curaEnv)$ pip install -r Cura/server/requirement.txt
(curaEnv)$ export CURA_SECRET_KEY='[local dev key]'
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

#### Server Directory Structure


##### Some Important Files
Files **synced** over github

- **requirement.txt** - python libraries used in this project, maintained by pip. please **update** this file if you install new librararies. ``` pip freeze > requirement.txt```
- **settings.py** - django project setting. don't put sensitive information into this file (e.g. SECRET_KEY, DB passwords).

Files **not synced** over github

- **local_settings.py** - django project setting on local machine. Put **sensitive** information in this setting file.
- **fieldkeys/** - keys for encrypted fields, **must** do so the project can work correctly [(detail)](https://github.com/shrimalmadhur/Cura/pull/7)

The working directory should look like this:

```
Under ../curaEnv/
curaEnv/
├── Cura/
├── bin/
│   └── activate (to activate working environment)
├── include/
└── lib/ 


Under ../curaEnv/Cura/server/
server/
├── djangoserver/
│   ├── cura/
│   ├── djangoserver/ (project setting dir)
│   │   ├── settings.py
│   │   └── local_settings.py
│   ├── manage.py (django-admin wrapper)
│   ├── sleep/ (Sleep Quality module)
│   ├── fieldkeys/ (Secret for Encrypted Fields)
│   └── [...]/ (additional modules)
└── requirement.txt 
```



[ionic]:http://ionicframework.com/docs/guide/installation.html
[node.js]:http://nodejs.org
[Django]:https://www.djangoproject.com
[iOS SDK]:https://developer.apple.com/devcenter/ios/index.action
[Android SDK]:http://developer.android.com/sdk/index.html
[angular.js]:http://angularjs.org
[cordova]:http://cordova.apache.org
[virtualenv]:https://virtualenv.pypa.io/en/latest/
[pip]: http://pip.readthedocs.org/en/stable/

