'use strict';

// Services

angular.module('anguportServices', ['ngResource'])

.factory('projectsFactory', ['$resource', function ($resource) {
    return $resource('http://localhost:5000/projects/:projectId', {}, {
        query: { method: 'GET', params: {projectId: ''}, isArray: true }
    });
}])

;