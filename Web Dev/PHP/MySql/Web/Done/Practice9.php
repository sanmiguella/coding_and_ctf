<?php

echo "<h4>Parameters inside GET superglobal:</h4>"; 
echo "<pre>";
print_r($_GET); 
echo "</pre>"; 

echo "<p>UserName : " . $_GET['UserName'] . "</p><hr>";

$cookieName = "PracticeCookie"; 
$cookieValue = 550; 
$cookieExpiry = time() + (60 * 60 * 24 * 7); // 60s(1min), 60min(1hr), 24hr(1day), 7day(1week)

setcookie($cookieName, $cookieValue, $cookieExpiry); // Set cookie to expire in a week.
echo "<p>Cookie $cookieName SET!</p>"; 
echo "<p>Cookie value : " . $_COOKIE[$cookieName] . "</p><hr>"; // Displays cookie name. 

session_start(); // Create session cookie.
$_SESSION['name'] = "Session 1"; 
$sessionName = $_SESSION['name']; 

echo "<pre>"; 
print_r($_SESSION); 
echo "</pre>"; 

echo "<p>Session name : $sessionName</p><hr>";

?>

<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Practice 9</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <link rel='stylesheet' href="MyCss.css" type='text/css'>
    
</head>
<body>


<div class="container">
    <div class="col-sm-6"> 

        <h2 class="text">Practice 9</h2><hr>

        <p><a href="Practice9.php?UserName=harry">Click Here!</a></p>
    </div>
</div>


</body>
</html>