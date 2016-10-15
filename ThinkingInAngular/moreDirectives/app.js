/**
 * Created by narendra on 10/10/16.
 */

var app = angular.module("moreDirectives", []);

app.controller("MoreDirectivesCtrl", MoreDirectivesCtrl );

function MoreDirectivesCtrl(){
    this.myList = [1,2,3,4,5,7];
    this.employees = [
        { 'name': 'Hello', 'age': 25},
        { 'name': 'Narendra', 'age': 105},
        { 'name': 'Avula', 'age': 52},
        { 'name': 'Naidu', 'age': 36},
        { 'name': 'Potta', 'age': 25}
    ]
}