<?php

include "db.php";

function list_items() {
    // $connection is a global scope variable from "db.php"
    global $connection;

    // Query to be passed to mysqli_query()
    $query = "SELECT * FROM  product"; 
    $result = query_check($query);

    // Creating of table headers.
    echo "<table border=1 width=30%>
                <tr>
                    <th>Product ID</th>
                    <th>Product Name</th>
                    <th>Price($)</th>
                    <th>Qty</th>
                </tr>";

    // List down all the products that exists on the database.
    while ($row = mysqli_fetch_assoc($result)) {
        $id = $row["id"];
        $product_name = $row["product_name"];
        $product_price = $row["product_price"]; 
        $product_qty = $row["product_qty"]; 
    
        // Inserting each row found in the database to the table.
        echo "<tr>
                <td>$id</td>
                <td>$product_name</td>
                <td>$product_price</td>
                <td>$product_qty</td>
            </tr>";
    }

    // Table closing tags.
    echo "</table><hr>";
}

function create_item($product_name, $product_price, $product_qty) {
    // $connection is a global scope variable from "db.php"
    global $connection; 
    
    /*
    Sample Query:

    $query  = "INSERT INTO users(username, password) ";
    $query .= "VALUES ('$username', '$password')";
    */
    $query  = "INSERT into product(product_name, product_price, product_qty) ";
    $query .= "VALUES ('$product_name', '$product_price', '$product_qty')";

    query_check($query);

    // Display a message to the user that the product has been created.
    echo "<p>$product_qty pieces of $product_name with a price tag of $product_price has been created!</p>";
}

function query_check($query) {
    // $connection is a global scope variable from "db.php"
    global $connection; 

    $result = mysqli_query($connection, $query); 

    if (!$result) {
        die("<br>QUERY failed!" . mysqli_error());
    }

    return $result;
}

?>