/**
 * Created by narendra on 6/9/16.
 */


/* example 1 */
// var myApp = angular.module('myModule', []);
//
// var myController = function ($scope) {
//   $scope.message =  "AnguularJS Tutorial";
// };
//
// myApp.controller("myController", myController );


/* example 2 */
// var myApp = angular.module('myModule', []);
//
// myApp.controller('myController', function ($scope) {
//
//     var employee = {
//         firstName : 'Narendra',
//         lastName : 'Avula',
//         gender : 'Male'
//     };
//
//     $scope.employee = employee;
//     $scope.message = "AngularJS Tutorial";
// });


/* example 3 */
// var myApp = angular
//             .module('myModule', [])
//             .controller('myController', function ($scope) {
//                 var employee = {
//                     firstName : 'Narendra',
//                     lastName : 'Avula',
//                     gender : 'Male'
//                 };
//
//                 $scope.employee = employee;
//                 $scope.message = "AngularJS Tutorial";
//             });

/* Video 4 */
//
// var myApp = angular
//             .module('myModule', [])
//             .controller('myController', function ($scope) {
//                 var country = {
//                     name : 'India',
//                     capital : 'New Delhi',
//                     flag : 'images/India.jpg'
//                 };
//                 $scope.country = country;
//
//             });


/* Video 5 */
//
// var myApp = angular
//             .module('myModule', [])
//             .controller('myController', function ($scope) {
//                 $scope.message = 'Hello Narendra!';
//             });


/* Video 6 */
// var myApp = angular
//             .module('myModule', [])
//             .controller('myController', function ($scope) {
//                 var employees = [
//                     {firstName:'Narendra', gender:'Male', salary:'5200'},
//                     {firstName:'Naidu', gender:'Male', salary:'25200'},
//                     {firstName:'Sister', gender:'Female', salary:'552200'},
//                     {firstName:'Potta', gender:'Female', salary:'35435200'}
//                 ];
//
//                 $scope.employees = employees;
//
//                 var countries = [
//                     {
//                         name: "UK",
//                         cities: [
//                             { name: "London" },
//                             { name: "Birmingham" },
//                             { name: "Manchester" }
//                         ]
//                     },
//                     {
//                         name: "USA",
//                         cities: [
//                             { name: "Los Angeles" },
//                             { name: "Chicago" },
//                             { name: "Houston" }
//                         ]
//                     },
//                     {
//                         name: "India",
//                         cities: [
//                             { name: "Hyderabad" },
//                             { name: "Chennai" },
//                             { name: "Mumbai" }
//                         ]
//                     }
//                 ];
//
//                 $scope.countries = countries;
//             });


/* Video 7 */
// var myApp = angular
//             .module('myModule', [])
//             .controller('myController', function ($scope) {
//                 var technologies = [
//                     {name: 'Python', likes:0, dislikes:0},
//                     {name: 'C#', likes:0, dislikes:0},
//                     {name: 'C++', likes:0, dislikes:0},
//                     {name: 'Java', likes:0, dislikes:0}
//                 ]
//
//                 $scope.technologies = technologies;
//
//                 $scope.incrementLikes = function (technology) {
//                     technology.likes++;
//                 };
//
//                 $scope.incrementDislikes = function (technology) {
//                     technology.dislikes++;
//                 };
//             });


/* Video 8 & 9 */
// var myApp = angular
//             .module('myModule', [])
//             .controller('myController', function ($scope) {
//                 var employees = [
//                     {
//                         name: "Ben", dateOfBirth: new Date("November 23, 1980"),
//                         gender: "Male", salary: 55000.788
//                     },
//                     {
//                         name: "Sara", dateOfBirth: new Date("May 05, 1970"),
//                         gender: "Female", salary: 68000
//                     },
//                     {
//                         name: "Mark", dateOfBirth: new Date("August 15, 1974"),
//                         gender: "Male", salary: 57000
//                     },
//                     {
//                         name: "Pam", dateOfBirth: new Date("October 27, 1979"),
//                         gender: "Female", salary: 53000
//                     },
//                     {
//                         name: "Todd", dateOfBirth: new Date("December 30, 1983"),
//                         gender: "Male", salary: 60000
//                     }
//                 ];
//
//                 $scope.employees = employees;
//                 $scope.rowCount = 5;
//                 $scope.sortColumn = "name";
//             });


/* Video 10 */
// var myApp = angular
//     .module('myModule', [])
//     .controller('myController', function ($scope) {
//         var employees = [
//             {
//                 name: "Ben", dateOfBirth: new Date("November 23, 1980"),
//                 gender: "Male", salary: 55000.788
//             },
//             {
//                 name: "Sara", dateOfBirth: new Date("May 05, 1970"),
//                 gender: "Female", salary: 68000
//             },
//             {
//                 name: "Mark", dateOfBirth: new Date("August 15, 1974"),
//                 gender: "Male", salary: 57000
//             },
//             {
//                 name: "Pam", dateOfBirth: new Date("October 27, 1979"),
//                 gender: "Female", salary: 53000
//             },
//             {
//                 name: "Todd", dateOfBirth: new Date("December 30, 1983"),
//                 gender: "Male", salary: 60000
//             }
//         ];
//
//         $scope.employees = employees;
//         $scope.sortColumn = "name";
//         $scope.reverseSort = false;
//
//         $scope.sortData = function (column) {
//             $scope.reverseSort = ($scope.sortColumn == column) ? !$scope.reverseSort : false;
//             $scope.sortColumn = column;
//         }
//
//         $scope.getSortClass = function (column) {
//             if ($scope.sortColumn == column) {
//                 return $scope.reverseSort
//                     ? 'arrow-down'
//                     : 'arrow-up';
//             }
//
//             return '';
//         }
//     });


/* Video 11 & 12 */
// var app = angular
//     .module("myModule", [])
//     .controller("myController", function ($scope) {
//
//         var employees = [
//             { name: "Ben", gender: "Male", salary: 55000, city: "London" },
//             { name: "Sara", gender: "Female", salary: 68000, city: "Chennai" },
//             { name: "Mark", gender: "Male", salary: 57000, city: "London" },
//             { name: "Pam", gender: "Female", salary: 53000, city: "Chennai" },
//             { name: "Todd", gender: "Male", salary: 60000, city: "London" },
//         ];
//
//         $scope.employees = employees;
//
//         $scope.search = function (item) {
//             if ($scope.searchText == undefined) {
//                 return true;
//             }
//             else {
//                 if (item.city.toLowerCase()
//                         .indexOf($scope.searchText.toLowerCase()) != -1 ||
//                     item.name.toLowerCase()
//                         .indexOf($scope.searchText.toLowerCase()) != -1) {
//                     return true;
//                 }
//             }
//
//             return false;
//         };
//     });


/* Video 13 */
var app = angular
    .module("myModule", [])
    .controller("myController", function ($scope) {

        var employees = [
            { name: "Ben", gender: 1, salary: 55000 },
            { name: "Sara", gender: 2, salary: 68000 },
            { name: "Mark", gender: 1, salary: 57000 },
            { name: "Pam", gender: 2, salary: 53000 },
            { name: "Todd", gender: 3, salary: 60000 }
        ];
        
        $scope.employees = employees;

    });