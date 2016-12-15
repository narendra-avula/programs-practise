/**
 * Created by narendra on 26/9/16.
 */

(function () {

    var module = angular.module("githubViewer");

    var RepoController = function ($scope, $routeParams, github) {

        var onRepos = function(data) {
            $scope.repos = data;
        };
        var onError = function(reason) {
            $scope.error = reason;
        };

        var reponame = $routeParams.reponame;
        var username = $routeParams.username;

        github.getRepoDetails(username, reponame)
            .then(onRepo, onError);
    };

    module.controller("RepoController", RepoController);
}());