/**
 * Created by narendra on 12/10/16.
 */

var myHelloModule = angular.module("myHelloModule", []);

myHelloModule.controller("HelloCtrl", HelloCtrl );

function HelloCtrl(){
    this.helloMessage = 'I am from myHelloModule Module';
}