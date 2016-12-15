/**
 * Created by narendra on 24/9/16.
 */

(function() {

    var app = angular.module("githubViewer");

    var UserController = function($scope, github, $routeParams) {

        console.log($routeParams);

        var onUserComplete = function (data) {
            $scope.user = data;
            github.getRepos($scope.user).then(onRepos, onError);
        };

        var onRepos = function (data) {
            $scope.repos = data;
        };

        var onError = function (reason) {
            $scope.error = "Could not fetch data.";
        };

        username = $routeParams.username ;
        github.getUser(username).then(onUserComplete, onError);
        $scope.repoSortOrder = "-stargazers_count";

    };

    app.controller("UserController", ["$scope", "github", UserController]);
}());
