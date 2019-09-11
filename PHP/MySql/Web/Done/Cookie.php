<?php

$cookieName = "MyCookie";
$cookieValue = 120; 

// Cookie set to expire in a week.
$cookieExpiry = time() + (60 * 60 * 24 * 7); // 60s(1min), 60m(1hr), 24hr(1day), 7days(1wk)

setcookie($cookieName, $cookieValue, $cookieExpiry);

if (isset($_POST["submit"])) {
    $myName = $_POST["myName"];
    
    if ($myName) {
        echo "<p>Name : $myName</p>";

        $secretCookieName = "MySecretCookie"; 
        $secretCookieValue = $myName;

        // Cookie set to expire in a month.
        $secretCookieExpiry = time() + (60 * 60 * 24 * 7 * 4); // 60s(1min), 60m(1hr), 24hr(1day), 7days(1wk), 4wks(1mth)

        setcookie($secretCookieName, $secretCookieValue, $secretCookieExpiry);

        echo "<p>Cookie <b>SET</b>!<hr>";
    } else {
        echo "<p>Name must not be empty!</p>";
    }
}

?>

<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Cookie</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <link rel='stylesheet' href="MyCss.css" type='text/css'>
    
</head>
<body>

<?php 

// Still buggy. 

if (isset($_COOKIE[$cookieName])) { // IF cookie is SET, assign cookie value to $cName.
    $cName = $_COOKIE[$cookieName];
} else {
    $cName = "<b>NOT SET!</b>"; // To be used for echo later.
}

echo "<p>Value 1 : $cName</p><hr>"; 

if (isset($secretCookieName)) { // IF cookie is set, assign cookie value to $scName.
    $scName = $_COOKIE[$secretCookieName]; 
} else {
    $scName = "<b>NOT SET!</b>"; // To be used for echo later.
}

echo "<p>Value 2 : $scName</p><hr>";

?>

<div class="container">
    <div class="col-sm-6"> 

        <h2 class="text">Cookie Creator</h2><hr>

        <form action="cookie.php" method="POST">
            <div class="form-group">
                <label for="myName">Name</label>

                <input type="text" class="form-control" name="myName">
            </div>

            <input class="btn btn-primary" type="submit" name="submit" value="Submit"> 
        </form> 
        
    </div>
</div>


</body>
</html>