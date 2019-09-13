var course = new Object(); // New object declaration

var course = {
    // Object properties
    title: "JavaScript Essential Training",
    instructor: "Morten Rand-Hendriksen",
    level: 1,
    published: true,
    views: 0,
    // Housing function inside an object
    updateViews: function() {
        return ++course.views; // When function runs, increment views by 1
    }
}

console.log(course); 

var current_date = new Date();  
var course_02 = new course(); // Reusing an object to declare a new object



