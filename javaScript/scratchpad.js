// console.log('Hello World again');
// console.log('Hello Java');

// var a = 10;
// var b = 20.0;
// var c = a + b;
// console.log(a);
// console.log(b);
// console.log(c);

// var a;
// console.log(a);

// a = false;
// // a = null;
// console.log(a);


// var TestVar;
// alert(TestVar); //shows undefined
// alert(typeof TestVar);

// var TestVar = null;
// alert(TestVar); //shows null
// alert(typeof TestVar); //shows object

// null === undefined // false
// null == undefined // true
// null === null // true

/*
Exception: prompt aborted by user
@440
*/

// console.log('Hello');

// console.log( typeof(null) ) Object

// var a = 10;
// var b = 10;
// if(a == b){
//     console.log("values are equal");
// } else {
//     console.log("values are not equal");
// }


// console.log(a + b);

// var a = 20;
// var b = 20;
// if (a == b) {
//     console.log("Variables are equal");
// }

/* OBJECTS */

// var myString = "Hello";

// var myObj = {};

// console.log(myObj);

// myObj.prop = 'Hello';

// console.log(myObj);

// myObj.name = 'Narendra';


// var myObj = {
// 'name':'narendra',
//  'job':'developer',
//  'objProp':{
//  'innerProp':'Inner Property'
// }
// };


// console.log(myObj.objProp);

// var myObj = {
// "myProp" : 'Hello'
// };

// var myObj2;
// myObj2 = myObj;

// console.log(myObj2.myProp);

// if(myObj === myObj2){
//     console.log('True');
// }


// var person = {
// 'firstName' : 'Narendra',
//  'lastName' : 'Avula',
//  'middleName' : null,
//  'age' : 25
// }

// console.log(person);

// delete person.age;

// console.log(person);

// var myArray = ['hello', 'narendra', 3, 6, 'JS'];
// console.log(myArray);
// myArray[2] = 'Naidu';
// console.log(myArray);

// function sayHello(){
//     console.log("Hello Narendra");
// }
// sayHello();


// function sayHello(name, day){
//     console.log("Hello " + name + 
//                  ", Time of the day is " + day);
// }
// sayHello('Naidu garu', 'Sunday');


// function sayHello(name, day){
//     console.log("Hello " + name + 
//                  ", Time of the day is " + day);
// }
// sayHello('Naidu garu');


// function sayHello(name, day){
//     console.log("Hello " + name + 
//                  ", Time of the day is " + day);
// }
// sayHello('Naidu garu','sunday', 'morning');

// function sayHello(name, day){
//     return "Hello " + name + 
//                  ", Time of the day is " + day;
// }
// var returnValue = sayHello('Naidu garu', 'Sunday');
// console.log(returnValue);

// var a = 'Hello';
// var f = function foo(){
//     console.log('Hello Naidu');
// };
// f();


// function foo(){
//     console.log('Hello Naidu foo func');
// }
// var f = function () {
//     console.log('Hello Naidu');
// };
// f();
// f = 1;
// f();


// var f = function () {
//     console.log('Hello Naidu');
// };
// var executor = function(fn){
//     console.log(fn);
// }
// executor(f);


// var f = function () {
//     console.log('Hello Naidu');
// };
// var executor = function(fn){
//     fn();
// }
// executor(f);

// var f = function (name) {
//     console.log('Hello, ' + name +' Naidu Avula');
// };
// var executor = function(fn, name){
//     fn(name);
// }
// executor(f, 'Narendra');

// var myObj = {
// 'testProp' : true
// };
// myObj.myMethod = function(){
//     console.log('functions as object');
// };
// console.log(myObj);
// myObj.myMethod();

// var person = {
// 'firstName' : 'Narendra',
//  'lastName' : 'Avula',
//  'getFullName' : function(){
//      return person.firstName +' '+ person.lastName;
//  }
// }

// var fullName = person.getFullName();
// console.log(fullName);


// var person = {
// 'firstName' : 'Narendra',
//  'lastName' : 'Avula',
//  'getFullName' : function(){
//      return this.firstName +' '+ this.lastName;
//  }
// }
// var fullName = person.getFullName();
// // console.log(fullName);
// var person2 = person;
// person = {};
// console.log(person2.getFullName());

// var person = {
//     'firstName' : 'Narendra',
//      'lastName' : 'Avula',
//      'getFullName' : function(){
//          return this.firstName +' '+ this.lastName;
//      },
//      'address':{
//          'street':'123 JS Street',
//          'city':'JS',
//          'state':'CA'
//     },
//      'isFromState' : function(state){
//          if (state == this.address.state){
//              return true;
//          } else {
//              return false;
//          }
//      } 
// };
// person.isFromState('CA');
// person.isFromState('AP');


// var add = function(){
//     var i, sum=0;
//     for (i =0 ; i < arguments.length; i++){
//         sum += arguments[i];
//     }
//     return sum;
// }
// console.log(add(2,3,4,5,6,7,10));

// var myArray = ['Hello', 'jasdhgfhs', 12, {}];
// myArray.push(5)
// myArray.pop()
// myArray.shift();
// myArray.unshift('Naidu');


// var myArray = ['Hello', 'jasdhgfhs', 'Naidu',12, {}];
// var myFunction = function(item){
//     console.log('For an element '+ item);
// }
// myArray.forEach(myFunction);


