/**
 * Created by narendra on 10/10/16.
 */

var module = angular.module("todoApp", []);
module.controller("TodoCtrl", TodoCtrl);

function TodoCtrl(){
    this.editMode = false;
    this.todos = [
        'Learn AngularJS',
        'Try out Excercises',
        'Visit JB Site'
    ];

    this.addNewTodo = function(){
        this.todos.push(this.newTodo);
        this.newTodo = '';
    };

    this.deleteTodo = function(index){
        this.todos.splice(index, 1);
    };

    this.triggerEditMode = function(){
        this.editMode = !this.editMode;
    };

}