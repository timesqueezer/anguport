'use strict';

// Services

angular.module('anguportServices', ['ngResource'])

.factory('projectsFactory', ['$resource', function ($resource) {
    return $resource('projects/:projectId.json', {}, {
        query: { method: 'GET', params: {projectId: 'projects'}, isArray: true }
    });
}])

;