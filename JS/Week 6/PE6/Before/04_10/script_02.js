// Object constructor
function Course(title, instructor, level, published, views) {
    this.title = title; 
    this.instructor = instructor; 
    this.level = level; 
    this.published = published; 
    this.views = views; 
    this.update_views = function() {
        return ++this.views; // Increments value by 1 and returns it
    };
}

// Assigning of values to variables which s to be passed when a new 
// instance of Course is created 
title = "Javascript Essential Training"; 
instructor = "Morten Rand-Hendriksen"; 
level = 1; 
published = true; 
views = 0; 

// Creating a new instance of Course, passing of values indirectly via variables
var course_01 = new Course(title, instructor, level, published, views);
console.log(course_01); // Display property values of course_01

// Passing of values directly into the object constructor
var course_02 = new Course("Up and running with ECMAScript 6", "Eve Porcello", 1, true, 123456); 

console.log(course_02); // Display property values of course_02

// Populate array with course objects
var courses = [
    course_03 = new Course("History of binary exploitation", "Me", 1, false, 0),
    course_04 = new Course("Wordpress hacking", "Me", 1, false, 0) 
]; 

console.log(courses); // Display the array of course objects

// Accessing the object array and its values 
console.log("Before update views: "); 
console.log(courses[0].views); 
console.log("After update views: "); 
console.log(courses[0].update_views());