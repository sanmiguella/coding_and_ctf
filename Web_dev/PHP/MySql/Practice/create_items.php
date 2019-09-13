<?php

include "functions.php";

if ( isset($_POST["create"]) ) {
    $product_name = $_POST["product_name"];
    $product_price = $_POST["product_price"]; 
    $product_qty = $_POST["product_qty"]; 

    if ($product_name && $product_price && $product_qty) {
        create_item($product_name, $product_price, $product_qty);
        list_items();
    }

    else {
        echo "<h4>Product name/price/qty must not be empty!</h4><hr>";
    }
}

?>

<!doctype html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Create Items</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <link rel='stylesheet' href='mycss.css' type='text/css'>
    
</head>
<body>

<form action="create_items.php" method="post">

    <h4 class="text">Create Items</h4><br>

    <div class="container">
        <div class="form-group">
            <label for="product_name"><b>Product Name</b></label>

            <input type="text" class="form-control col-sm-6" name="product_name">
        </div>

        <div class="form-group">
            <label for="product_price"><b>Product Price</b></label>

            <br>
            <input type="number" step="0.05" name="product_price">
        </div>

        <div class="form-group">
            <label for="product_qty"><b>Product Qty</b></label>

            <br>
            <input type="number" min=1 max=10 name="product_qty">
        </div>

        <input class="btn btn-primary" type="submit" name="create" value="Create"> <!-- btn & btn-primary to make buttons looks nicer -->
    </div>
</form> 


</body>
</html>