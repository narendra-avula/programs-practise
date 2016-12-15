/**
 * Created by narendra on 10/10/16.
 */

var app = angular.module("modulesApp", ['myHelloModule', 'ngTagsInput']);

app.controller("TagsDemoCtrl", TagsDemoCtrl);

function TagsDemoCtrl(){
    this.tags = [
        { text: 'Test1'},
        { text: 'Test2'},
        { text: 'Test3'},
        { text: 'Test4'},
    ]
}

//app.controller("HelloCtrl", HelloCtrl );
//
//function HelloCtrl(){
//    this.helloMessage = 'I am from Main Module';
//}

