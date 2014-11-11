'use strict';

// Services

angular.module('anguportServices', ['ngResource'])

.factory('projectsFactory', ['$resource', function ($resource) {
    return $resource('/api/:projectId', {}, {
        query: { method: 'GET', params: {projectId: ''}, isArray: true }
    });
}])

;