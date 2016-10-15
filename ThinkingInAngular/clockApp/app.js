/**
 * Created by narendra on 10/10/16.
 */

var module = angular.module("myApp", []);
module.controller("ClockCtrl", getTime);

function getTime($scope, $timeout){
    $scope.heading = "Clock APP";
    $scope.clock = "loading clock...";
    $scope.tickInterval = 1000;

    var tick = function(){
        $scope.clock = new Date();
        $timeout(tick, $scope.tickInterval);
    };

    $timeout(tick, $scope.tickInterval);
}