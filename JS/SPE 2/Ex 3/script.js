// Object constructor for Members object
function Members(id, name, date_of_birth, address, mobile_num) {
    this.id = id; 
    this.name = name;
    this.date_of_birth = date_of_birth; 
    this.address = address; 
    this.mobile_num = mobile_num; 
}

// Populate membership Array with Members object
var membership = [ 
    new Members(1, "Alex", "01-02-1990", "Addr 1", "+65 9090 0000"),
    new Members(2, "Tom", "02-02-1990", "Addr 2", "+65 9191 0101"),
    new Members(3, "Dick", "03-02-1990", "Addr 3", "+65 9292 0202")
];

// Array starts with 0 
var i = 0,  str_alert = ""; 
while (i < membership.length) { // membership.length is 3 but array starts with 0, so the upper bound is 2
    // To make the data look sensible when alert() is called
    str_alert += "ID: " + membership[i].id; 
    str_alert += " , NAME: " + membership[i].name;
    str_alert += " , DOB: " + membership[i].date_of_birth; 
    str_alert += " , MOBILE: " + membership[i].mobile_num; 
    str_alert += "\n"; // After each array element/loop iteration, a newline is printed

    i++; // To prevent while from going into a continuous loop
}

alert(str_alert);