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
    $scope.addProject = function () {
        var title = $scope.newProject.title;
        var desc = $scope.newProject.desc;
        
        var new_p = new projectsFactory({'projectId': title, 'title': title, 'desc': desc });
        var resp = new_p.$save({projectId: ''});
        $scope.projects = projectsFactory.query();
    };
    
    $scope.delProject = function (id) {
        projectsFactory.delete({projectId: id});
        $scope.projects = projectsFactory.query();
    };
    
}])

.controller('projectDetailController', ['$scope', '$routeParams', 'projectsFactory', function ($scope, $routeParams, projectsFactory) {
    $scope.project = projectsFactory.get({ projectId: $routeParams.projectId});
}])

;