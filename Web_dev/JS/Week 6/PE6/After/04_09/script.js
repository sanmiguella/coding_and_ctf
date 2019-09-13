var course = new Object(); // Creates new javascript object

/** Object properties {long- hand}
course.title = "JavaScript Essential Training"; 
course.instructor = "Morten Rand-Hendriksen"; 
course.level = 1; 
course.published = true; 
course.views = 0;
**/

// Object properties {short-hand}
var course = {
    title: "Javascript Essential Training",
    instructor: "Morten Rand-Hendriksen",
    level: 1, 
    published: true,
    views: 0, 

    update_views: function() {
        return ++course.views; // Increment views by 1
    }
}

console.log("Display all object properties:");
console.log(course); // Display all the object properties in a console

console.log("Before update_views() being called:"); 
console.log(course.views); // Before update_views() called
console.log("After update_views() are called:");
course.update_views();  // Calls the update_views() 
console.log(course.views); // After update_views() called

display_object(); // Calls a function to display object properties on a screen

function display_object() {
    msg = "<h2>Object -> Course</h2>"; 
    msg += "<b>Object properties:</b><br><br>"; 

    // Keep in mind that the properties of an object can be accessed with course.x where
    // course is the object 
    msg += "title: " + "<u>" + course.title + "</u><br>"; 
    msg += "instructor: " + "<u>" + course.instructor + "</u><br>"; 
    msg += "level: " + "<u>" + course.level + "</u><br>"; 
    msg += "published: " + "<u>" + course.published + "</u><br>";
    msg += "views: " + "<u>" + course.views + "</u><br>"; 

    document.body.innerHTML = msg;     
}