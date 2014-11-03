'use strict';

// Controllers

angular.module('anguportControllers', [])

.controller('menuController', function ($scope) {
    $scope.menuitems = [
        {l: '/', t: 'Home'},
        {l: '/about', t: 'About'},
        {l: '/projects', t: 'Projects'},
        {l: '/contact', t: 'Contact'}
    ];
})

.controller('staticController', function ($scope) {

})

.controller('projectListController', ['$scope', 'projectsFactory', function ($scope, projectsFactory) {
    $scope.projects = projectsFactory.query();
    
}])

.controller('projectDetailController', ['$scope', '$routeParams', 'projectsFactory', function ($scope, $routeParams, projectsFactory) {
    $scope.project = projectsFactory.get({ projectId: $routeParams.projectId});
}])

;