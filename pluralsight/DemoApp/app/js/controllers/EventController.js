/**
 * Created by narendra on 27/9/16.
 */
'use strict';

eventsApp.controller('EventController',
    function EventController($scope) {

        $scope.snippet = '<span style="color:red">Hi there</span>';
        $scope.boolValue = false;
        $scope.buttonDisabled = true;
        $scope.event = {
            name : 'Angular Js demo',
            date : '27/09/2016',
            time : '12.30 PM',
            location : {
                address : 'Google Headquarters',
                city : 'Moutain View',
                provience : 'CA'
            },
            imageUrl:'img/angularjs-logo.png',
            sessions : [
                {
                    name : 'Directives Masterclass',
                    creatorName : 'Narendra Avula',
                    duration : '3 HR 15 MINS',
                    level : 'Basic',
                    abstract : 'In this session you will learn the ins and outs of directives!',
                    upVoteCount : 3
                },
                {
                    name : 'Scopes for fun and profit',
                    creatorName : 'Potta Deepthi',
                    duration : '15 Mins',
                    level : 'Medium',
                    abstract : 'will take a closer look at scope',
                    upVoteCount : 15
                },
                {
                    name : 'Well behaved controllers',
                    creatorName : 'Naidu',
                    duration : '5 HR',
                    level : 'Advanced',
                    abstract : 'Full tutorial of Angular JS',
                    upVoteCount : 8
                }
            ]
        }

        $scope.upVoteSession = function (session) {
            session.upVoteCount++;
        };

        $scope.downVoteSession = function (session) {
            session.upVoteCount--;
        };
    }
);