/**
 * Created by narendra on 24/9/16.
 */

(function(module) {
    module.config(function($routeProvider) {
        $routeProvider
            .when("/main", {
                templateUrl: "main.html",
                controller: "MainController"
            })
            .when("/user/:username", {
                templateUrl: "user.html",
                controller: "UserController"
            })
            .when("/repo:username/:reponame", {
                templateUrl: "repo.html",
                controller: "RepoController"
            })
            .otherwise({redirectTo: "/main"})
    });

}(angular.module("githubViewer", ["ngRoute"])));