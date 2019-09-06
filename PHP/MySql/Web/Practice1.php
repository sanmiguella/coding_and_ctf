<?php

// Shows $_GET array values properly formatted.
echo "<pre>";

print_r($_GET);

echo "</pre>";
echo "<hr>";

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

        <h4 class="text">Practice 1</h4><br>

        <!-- Setting the dynamic values -->
        <?php 
            $id = 50;
            $link_1 = "Click here for link 1"; 
            $link_2 = "Click here for link 2";
            $link_3 = "Click here for link 3";
        ?>

        <!-- Dynamic values -->

        <p><a href="Practice1.php?id=<?php echo $id; ?>"><?php echo $link_1; ?></a></p>

        <p><a href="Practice1.php?id=<?php echo $id; ?>&health=healthy"><?php echo $link_2; ?></a></p>

        <p><a href="Practice1.php?id=<?php echo $id; ?>&health=healthy&mood=happy"><?php echo $link_3; ?></a></p>
        
    </div>
</div>


</body>
</html>