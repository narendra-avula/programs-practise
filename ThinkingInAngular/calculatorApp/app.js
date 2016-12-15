/**
 * Created by narendra on 10/10/16.
 */

var app = angular.module("calculator", []);

app.controller("CalculatorCtrl", getCalculator, getOperator );

function getCalculator($scope){
    $scope.operator = ' ';
    $scope.addition = "+";
    $scope.subtract = "-";
    $scope.multi = "*";
    $scope.divide = "/";
}

function getOperator(operator){
    console.log(operator);
}