<?php


?>

<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Template</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <link rel='stylesheet' href="MyCss.css" type='text/css'>
    
</head>
<body>

<div class="container">
    <div class="col-sm-6"> 

        <h4 class="text">Template</h4><br>

        <form action="Template.php" method="GET">
            <div class="form-group">
                <label for="username">Username</label>

                <input type="text" class="form-control" name="username">
            </div>

            <div class="form-group">
                <label for="password">Password</label>

                <input type="password" class="form-control" name="password">
            </div>

            <br>
            <input class="btn btn-success" type="submit" name="login" value="Login"> 
        </form> 
        
    </div>
</div>


</body>
</html>