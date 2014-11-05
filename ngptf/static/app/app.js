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
            templateUrl: 'static/views/home.html'
        })
        .when('/about', {
            controller: 'staticController',
            templateUrl: 'static/views/about.html'
        })
        .when('/contact', {
            controller: 'staticController',
            templateUrl: 'static/views/contact.html'
        })
        .when('/projects', {
            controller: 'projectListController',
            templateUrl: 'static/views/projects.html'
        })
        .when('/projects/:projectId', {
            controller: 'projectDetailController',
            templateUrl: 'static/views/project.html'
        })
        .otherwise({ redirectTo: '/' });
}])

;