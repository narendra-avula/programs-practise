/**
 * Created by narendra on 9/9/16.
 */

(function(module) {

    var MainController = function($scope, $interval, $location, $log) {

        var decrementCountdown = function() {
            $scope.countdown -= 1;

            if ($scope.countdown < 1) {
                $scope.search($scope.username);
            }
        };

        var countDowninterval = null;
        var startCountdown = function() {
            countDowninterval = $interval(decrementCountdown, 1000, $scope.countdown);

        };

        $scope.search = function(username) {
            if (countDowninterval) {
                $interval.cancel(countDowninterval);
                $scope.countdown = null;
            }

            //Search
            $log.log("Searching...")
            $location.path("/user/" + username);
        };
        $scope.username = "angular";
        $scope.countdown = 5;
        startCountdown();
    };

    module.controller("MainController", MainController);

}(angular.module("githubViewer")));

// var result = 2 + 5;

// alert(result);
//
// (function () {
//
//     var app = angular.module("githubViewer", []);
//
//     var MainController = function (
//         $scope, $github, $interval, $log, $anchorScroll, $location) {
//
//         var onUserComplete = function (data) {
//             $scope.user = data;
//             github.getRepos($scope.user).then(onRepos, onError);
//         };
//
//         var onRepos = function (response) {
//             $scope.repos = response.data;
//             $location.hash("userDetails");
//             $anchorScroll();
//         };
//
//         var onError = function (reason) {
//             $scope.error = "Could not fetch the data";
//         };
//
//         var decrementCountdown = function () {
//             $scope.countdown -= 1;
//             if ($scope.countdown < 1){
//                 $scope.search($scope.username)
//             }
//         };
//
//         var countdownInterval = null;
//         var startCountDown = function () {
//             countdownInterval = $interval(decrementCountdown, 1000, $scope.countdown);
//         };
//
//         $scope.search = function (username) {
//             $log.info("searching for " + username);
//             github.getUser(username).then(onUserComplete, onError);
//             if (countdownInterval){
//                 $interval.cancel(countdownInterval);
//                 $scope.countdown = null;
//             };
//         };
//
//
//         $scope.username = "narendradivi";
//         $scope.message = "GitHub Viewer";
//         $scope.repoSortOrder = "stargazers_count";
//         $scope.countdown = 5;
//         startCountDown();
//     };
//
//     app.controller("MainController", MainController);
//
// }());



// var myApp = angular.module('myApp', []);
//
// var module = angular.module("HttpController");
//
// myApp.controller('MainController', function ($scope) {
//     var person = {
//         firstName : 'Narendra',
//         lastName :'Avula'
//     }
//     $scope.message = "Hello , Narendra!!";
// });
//
//
// myApp.controller('SubController', function ($scope) {
//     $scope.message = "Hello , Potta!!";
// });
//
//
// myApp.controller('HttpController', function (
//     $scope, $github, $interval, $log, $anchorScroll, $location) {
//
//     var onUserComplete = function (data) {
//         $scope.user = data;
//         github.getRepos($scope.user).then(onRepos, onError);
//     };
//
//     var onRepos = function (response) {
//         $scope.repos = response.data;
//         $location.hash("userDetails");
//         $anchorScroll();
//     };
//
//     var onError = function (reason) {
//         $scope.error = "Could not fetch the data";
//     };
//
//     var decrementCountdown = function () {
//         $scope.countdown -= 1;
//         if ($scope.countdown < 1){
//             $scope.search($scope.username)
//         }
//     };
//
//     var countdownInterval = null;
//     var startCountDown = function () {
//         countdownInterval = $interval(decrementCountdown, 1000, $scope.countdown);
//     };
//
//     $scope.search = function (username) {
//         $log.info("searching for " + username);
//         github.getUser(username).then(onUserComplete, onError);
//         if (countdownInterval){
//             $interval.cancel(countdownInterval);
//             $scope.countdown = null;
//         };
//     };
//
//
//     $scope.username = "narendradivi";
//     $scope.message = "GitHub Viewer";
//     $scope.repoSortOrder = "stargazers_count";
//     $scope.countdown = 5;
//     startCountDown();
//
// });


