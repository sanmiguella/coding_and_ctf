<?php

echo "<pre>"; 
print_r($_POST); // Prints the value contained inside the $_POST superglobal.
echo "</pre>";

if (isset($_POST["submit"])) { // IF submit button is pressed.
    $myName = $_POST["myName"]; // Assigns the value from input textbox into a variable.

    if ($myName) { // IF $myName is not empty.
        echo "<p>Your name is : <b>$myName</b></p>"; 
    } else { // IF $myName is empty.
        echo "<p>You didn't enter any name!</p>";
    }
}

echo "<hr>"; 

?>

<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Post 1</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <link rel='stylesheet' href="MyCss.css" type='text/css'>
    
</head>
<body>

<div class="container">
    <div class="col-sm-6"> 

        <h4 class="text">Post 1</h4><hr>

        <form action="post1.php" method="post"> 
            <label for="name">Name</label>

            <div class="form-group">
                <!-- Class: form-control is important, it makes the input textbox longer and more aesthetically pleasing -->
                <p><input type="text" class="form-control" name="myName" placeholder="$myName variable"></p>
            </div>

            <input class="btn btn-primary" type="submit" name="submit" value="submit">
        </form>
        
    </div>
</div>


</body>
</html>