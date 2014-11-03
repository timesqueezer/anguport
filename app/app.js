'use strict';

// App

angular.module('anguport', [
    'ngRoute',
    'anguportControllers',
    'anguportServices'
])

.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/', {
            controller: 'staticController',
            templateUrl: 'views/home.html'
        })
        .when('/about', {
            controller: 'staticController',
            templateUrl: 'views/about.html'
        })
        .when('/contact', {
            controller: 'staticController',
            templateUrl: 'views/contact.html'
        })
        .when('/projects', {
            controller: 'projectListController',
            templateUrl: 'views/projects.html'
        })
        .when('/projects/:projectId', {
            controller: 'projectDetailController',
            templateUrl: 'views/project.html'
        })
        .otherwise({ redirectTo: '/' });
}])

;