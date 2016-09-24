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
      .otherwise({redirectTo: "/main"})
  });

}(angular.module("githubViewer", ["ngRoute"])));