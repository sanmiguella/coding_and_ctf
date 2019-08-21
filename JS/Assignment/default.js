function product(prod_id, name, desc, price, stock, image) 
{
    this.prod_id = prod_id; // Product ID.
    this.name = name; // Product Name.
    this.desc = desc; // Product Description.
    this.price = price; // Price of product.
    this.stock = stock; // Amount of stock.
    this.image = image; // Value to hold the product's image.
}

function cart(prod_id, name, price, qty, subtotal)
{
    this.prod_id = prod_id; // Product ID.
    this.name = name; // Product Name.
    this.price = price; // Price of product.
    this.qty = qty; // Current quantity.
    this.subtotal = subtotal; // To hold current subtotal.
}

function clear_search_table() 
{
    // Delete all the table rows
    for (i = table_search.rows.length - 1; i > 0; i--) {
        table_search.deleteRow(i);
    }
}

function clear_entry() 
{
    // Empties the values inside all of the textboxes.
    document.getElementById("prod_id").value = "";
    document.getElementById("name").value = "";
    document.getElementById("desc").value = "";
    document.getElementById("price").value = "";
    document.getElementById("stock").value = "";
    document.getElementById("image").value = "";
}

function clear_table() 
{
    // Delete all the table rows.
    for (i = table.rows.length - 1; i > 0; i--) {
        table.deleteRow(i);
    }
}

function clear_cart_listing() 
{
    // Delete all the table rows.
    for (i = table_cart.rows.length - 1; i > 0; i--) {
        table_cart.deleteRow(i);
    }
}

function populate_search_table(found_product) {
    // Number of elements in an array
    var upper_bound = found_product.length;

    for(i = 0; i < upper_bound; i++) {
        // Creates row.
        var row = table_search.insertRow(i + 1);

        // Creates cell.
        var cell_prod_id = row.insertCell(0)
        var cell_prod_name = row.insertCell(1);
        var cell_desc = row.insertCell(2);
        var cell_price = row.insertCell(3);
        var cell_stock = row.insertCell(4);

        // Assign value to cell.
        cell_prod_id.innerHTML = found_product[i].prod_id;
        cell_prod_name.innerHTML = found_product[i].name;
        cell_desc.innerHTML = found_product[i].desc;
        cell_price.innerHTML = found_product[i].price;
        cell_stock.innerHTML = found_product[i].stock;
    }
}

function populate_table()
{
    // Number of elements in an array
    var upper_bound = product_array.length;

    /* 
        If table is not cleared, the table entry will keep on growing, 
        after every call to populate_table().
    */
    clear_table();

    for(i = 0; i < upper_bound; i++) {
        // Creates Row.
        var row = table.insertRow(i + 1);

        // Creates Cell.
        var cell_prod_id = row.insertCell(0);
        var cell_name = row.insertCell(1);
        var cell_desc = row.insertCell(2);
        var cell_price = row.insertCell(3);
        var cell_stock = row.insertCell(4);
        var cell_image = row.insertCell(5);
        var cell_actions = row.insertCell(6);

        // Populates every cell with data that corresponds with values in product_array[]
        cell_prod_id.innerHTML = product_array[i].prod_id;
        cell_name.innerHTML = product_array[i].name;
        cell_desc.innerHTML = product_array[i].desc;
        cell_price.innerHTML = product_array[i].price;
        cell_stock.innerHTML = product_array[i].stock;
        cell_image.innerHTML = product_array[i].image;

        // Creating of edit and delete buttons.
        cell_actions.innerHTML = 
        "<td>\
            <input type='button' value='Edit' onclick='edit_row(this)'></button>\
            <input type='button' value='Delete' onclick='delete_row(this)'></button>\
        </td>";
    }

    populate_table_listing();
    console.log(product_array);
}

function populate_table_listing()
{
    table_listing.innerHTML = ""; // Prevents table from stacking up.
    var upper_bound = product_array.length; // Number of elements in an array.
    var items_per_row = 4; // Items per row.
    var html = "<table id='prod_list'><tr>";

    /**
     ROW: horizontal
     COL: vertical
    * */
    for (i = 0; i < upper_bound; i++) {
        html += "<td>";
        html += "<img src='" + product_array[i].image + "' height=185 width=195><br>";
        html += "ID: " + product_array[i].prod_id + "<br>"
        html += "Item: " + product_array[i].name + "<br>";
        html += "<b>"+ product_array[i].desc + "</b></br>";
        html += "Price: <i>$" + product_array[i].price + "</i><br>";
        html += "Qty: <u>" + product_array[i].stock + "</u><br><br>";
        html += "<input type='button' value='Add to cart' onclick='add_to_cart(this)'></button>";
        html += "</td>";

        var next = i + 1;

        /**
            Loop 0 -> next 1 -> 1
            Loop 1 -> next 2 -> 2
            Loop 2 -> next 3 -> 3
            Loop 4 -> next 4 -> 0
        * */
        if (next%items_per_row == 0 && next != upper_bound) {
            html += "</tr><tr>";
        }
    }

    html += "</tr></table>";
    table_listing.innerHTML = html;
}

function populate_cart_listing()
{
    clear_cart_listing();

    var upper_bound = cart_array.length;
    //var grand_total = 0;
    grand_total = 0;

    for (i = 0; i < upper_bound; i++) {
        // Creates row.
        var row = table_cart.insertRow(i + 1);

        // Creates cell.
        var cell_prod_name = row.insertCell(0);
        var cell_price = row.insertCell(1);
        var cell_qty = row.insertCell(2);
        var cell_subtotal = row.insertCell(3);
        var cell_action = row.insertCell(4);

        // Assign value to cell.
        cell_prod_name.innerHTML = cart_array[i].name;
        cell_price.innerHTML = cart_array[i].price;
        cell_qty.innerHTML = cart_array[i].qty;
        cell_subtotal.innerHTML = cart_array[i].subtotal;

        // Creates delete button.
        cell_action.innerHTML = "\
        <td>\
            <input type='button' value='Delete' onclick='delete_cart_items(this)'></button>\
        </td>";

        /*
             On every iteration, add the current subtotal to grand_total so that,
             when the for loop ends, the grand_total is the sum of all subtotal.
        */
        grand_total += cart_array[i].subtotal; 

        if (upper_bound - i == 1) { // If it is the last item, add a payable amount.
            row = table_cart.insertRow(i + 2);
            row.innerHTML = "<td colspan='3'><b>Total Payable ($)</b></td>\
            <td><b>" + grand_total + "</b></td>\
            <td><input type='button' value='Empty cart' onclick='empty_cart()'></button>\
                <input type='button' value='Buy' onclick='purchase()'></button></td>";

            row = table_cart.insertRow(i + 3);
            row.innerHTML = "<td colspan='5'><div id='paypal-button-container'></div></td>";
        }
    }
}

function add_to_cart(index) 
{
    var current_row = index.closest('tr').rowIndex; // Determine the current row.
    var current_cell = index.closest('td').cellIndex + 1; // Determine the current cell.
    var current_selection = (4 * current_row) + current_cell - 1; // Determine the current selection.
    
    var prod_id = product_array[current_selection].prod_id;
    var name = product_array[current_selection].name;
    var stock = product_array[current_selection].stock;   

    // For initial adding of items into cart.
    var price = product_array[current_selection].price; // For subtotal.
    var qty = 1; // Initial quantity
    var subtotal = price * qty;  // Initial subtotal

    if (cart_array.length  > 0 ) { // If shopping cart has items in it.
        var found = false;
        var item_found_number;

        for (var item in cart_array) {
            if (cart_array[item].prod_id == prod_id) {

                item_found_number = item;
                found = true;
                break; // If item is found, exit for loop.
            }
        }

        if (!found) { // If item is not found in the shopping cart, add item to cart.
            product_array[current_selection].stock = stock - 1;

            current_cart = new cart(prod_id, name, price, qty, subtotal);
            cart_array.push(current_cart);
        }

        else { // If item is found in shopping cart.
            if (stock > 0) { // If there is still stock for the selected item.
                product_array[current_selection].stock = stock - 1;

                cart_array[item_found_number].qty += 1; // Increments the qty of the added items by 1.
                cart_array[item_found_number].subtotal = cart_array[item_found_number].price * cart_array[item_found_number].qty;
            } 
            
            else { // If there is no more stock for the selected item.
                var error_msg = "";
                
                error_msg = "No more stock for now :(";
                alert(error_msg);
            }
        }
    }

    else { // If shopping cart doesn't have items in it.
        /*
            Even if we add new product to shopping cart, we have to decrement stock by 1,
            else quantity will get bugged out and wont tally on the shopping cart for ex:
            max stock: 5 , shopping cart qty: 6
        */
        product_array[current_selection].stock = stock - 1;

        // cart(prod_id, price, qty, subtotal)
        current_cart = new cart(prod_id, name, price, qty, subtotal);
        cart_array.push(current_cart);
    }

    populate_table_listing();
    populate_cart_listing();    
}

function delete_cart_items(index) 
{
    var row_index = index.parentNode.parentNode.rowIndex; // Current index on the table.
    var cart_index = index.parentNode.parentNode.rowIndex - 1; // The index of selected row in cart_array[].
    var prod_id = cart_array[cart_index].prod_id; // To be used for searching product_array[] later.
    var cart_array_qty = cart_array[cart_index].qty; // To be added to product_array[] stock.
    var item_found_number;

    for (var item in product_array) {
        if (product_array[item].prod_id == prod_id) {

            item_found_number = item;
            break; // If item is found, exit for loop.
        }
    }

    // When item is deleted from row, the original quantity should be restored.
    product_array[item_found_number].stock += cart_array_qty;

    table_cart.deleteRow(row_index); // Deletes current row.
    cart_array.splice(row_index - 1, 1); // Removes said row from cart_array[].

    populate_table_listing();
    populate_cart_listing();
}

function empty_cart()
{
    upper_bound = cart_array.length;

    for (i = 0; i < upper_bound; i++) {            
        var prod_id = cart_array[i].prod_id; // Cart product id to be used for searching product_array[].
        var cart_array_qty = cart_array[i].qty; // For restoration of original quantity.

        for (var item in product_array) {
            if (product_array[item].prod_id == prod_id) {

                product_array[item].stock += cart_array_qty;
                break; // If item is found update quantity and exit for loop.
            }
        }
    }

    cart_array = []; // Empties the array.

    populate_cart_listing();
    populate_table_listing();

    alert("Cart emptied.");
}

function add_product() 
{
    // If update_lock == false
    if (!update_lock) {

        // To simplify accessing DOM property.
        txtbox_prod_id = document.getElementById("prod_id").value;
        txtbox_prod_name = document.getElementById("name").value;
        txtbox_prod_desc = document.getElementById("desc").value;
        txtbox_prod_price = document.getElementById("price").value;
        txtbox_prod_stock = document.getElementById("stock").value;
        txtbox_prod_image = document.getElementById("image").value;

        var contains_error = validate(txtbox_prod_id, txtbox_prod_name, txtbox_prod_desc, txtbox_prod_price, txtbox_prod_stock, txtbox_prod_image);

        // If there are no errors add entries to the array.
        if (!contains_error) {
            new_product = new product(
                txtbox_prod_id,
                txtbox_prod_name,
                txtbox_prod_desc,
                txtbox_prod_price,
                txtbox_prod_stock,
                txtbox_prod_image
            );

            // Adds entries to the product_array[]
            product_array.push(new_product);
        }

        populate_table();
        clear_entry();
    }

    else {
        alert("Update must be completed before adding new product.");
    }
}

function update() 
{
    if (update_lock) {

        // To simplify accessing DOM property
        txtbox_prod_id = document.getElementById("prod_id").value;
        txtbox_prod_name = document.getElementById("name").value;
        txtbox_prod_desc = document.getElementById("desc").value; 
        txtbox_prod_price = document.getElementById("price").value;
        txtbox_prod_stock = document.getElementById("stock").value;
        txtbox_prod_image = document.getElementById("image").value

        // validate(prod_id, name, desc, price, stock, image)
        var contains_error = validate(txtbox_prod_id, txtbox_prod_name, txtbox_prod_desc,txtbox_prod_price, txtbox_prod_stock, txtbox_prod_image);

        // If there are no errors update entries of the array.
        if (!contains_error) {
    
            // Update product_array[] according to the values in the entry box.
            product_array[update_index].prod_id = txtbox_prod_id;
            product_array[update_index].name = txtbox_prod_name;
            product_array[update_index].desc = txtbox_prod_desc;
            product_array[update_index].price = txtbox_prod_price; 
            product_array[update_index].stock = txtbox_prod_stock;
            product_array[update_index].image = txtbox_prod_image;
    
            alert("Updated.");

            update_lock = false; // After update is successful, unflag update_lock
            update_index = -1;
    
            populate_table(); // List updated table after update.
            clear_entry(); // Clear textbox entries after successful update.
    
            /*
             After update is successful update button is disabled,
             add button is enabled, clear button is enabled.
            */
            btn_update.disabled = true;
            btn_add.disabled = false;
            btn_clear.disabled = false;    
        }
    }
}

function delete_row(index) 
{
    if (!update_lock) {
        var i = index.parentNode.parentNode.rowIndex; 

        table.deleteRow(i); // Deletes the current row.
        product_array.splice(i - 1, 1); // Removes the said row from the product_array[]
        
        /*
            If delete is successfully done, unflag update_lock,
            disable the update button, enable the add button,
            enable the clear button.
        */
        update_lock = false;
        btn_update.disabled = true;
        btn_add.disabled = false;
        btn_clear.disabled = false;
        
        // Clears entry after row is sucessfully deleted.
        clear_entry();
    } 

    else { // update_lock == true
        var error_msg = "";

        error_msg = "Update(s) to Product id " + product_array[update_index].prod_id + " has not been completed.\n";
        error_msg += "Delete failed.";
        alert(error_msg);
    }

    populate_table();
}

function edit_row(index)    
{
    if (entry.style.display != "none") {
        var i = index.parentNode.parentNode.rowIndex - 1; 

        /*
            Populates the entry form according to the values,
            contained inside product_array[]
        */
        document.getElementById("prod_id").value = product_array[i].prod_id;
        document.getElementById("name").value = product_array[i].name;
        document.getElementById("desc").value = product_array[i].desc;
        document.getElementById("price").value = product_array[i].price;
        document.getElementById("stock").value = product_array[i].stock;
        document.getElementById("image").value = product_array[i].image;

        update_lock = true; // If edit button is clicked update_lock is flagged as true.

        // To identify the proper index of the product_array[] according to the row being edited.
        update_index = i; 

        /*
            If edit button is pressed, update button is enabled,
            add button is disabled and clear button is disabled.
        */
        btn_update.disabled = false;
        btn_add.disabled = true;
        btn_clear.disabled = true;
    }

    else {
        alert("Please click 'Add Products' first.");
    }
}

function search_display_table() {
    table_search.style.display = "table";
    table.style.display = "none";
    entry.style.display = "none";

    var item_found_number = [], found = false;
    var prod_name = prompt("Please enter product name:"); // Prompts user for input, eg: product name.

    if ((prod_name != "") && (prod_name != null)) { // If product name is not empty and null(cancel).
        for (var item in product_array) {
            if (product_array[item].name == prod_name) {
                /*
                    For every item that is found, determine its index and store it in 
                    an array.
                */
                item_found_number.push(parseInt(item)); // parseInt() -> Convert strings to integers.
                found = true;
            }
        }

        if (found) { // If item is found
            var found_product = [];

            for (i = 0; i < item_found_number.length; i++) {
                /*
                    For every item that is found, the object values from the corresponding index
                    of the product_array[], will be stored in the found_product[] array.
                */
                found_product[i] = new product( 
                    product_array[ item_found_number[i] ].prod_id,
                    product_array[ item_found_number[i] ].name,
                    product_array[ item_found_number[i] ].desc,
                    product_array[ item_found_number[i] ].price,
                    product_array[ item_found_number[i] ].stock,
                    product_array[ item_found_number[i] ].image
                );
            }

            clear_search_table();
            populate_search_table(found_product);
        } 

        else {
            var error_msg = prod_name + " not found.";
            alert(error_msg);

            clear_search_table();
        } 
    }

    else {
        alert("Product name must not be empty.");
    }
}

function validate(prod_id, name, desc, price, stock, image)
{
    var error_message = "";
    var contains_error = false;

    /*
     If any of the parameters are empty, contains_error is flagged as true,
     and after all the checking is done, alerts user of the error that user,
     has made.
    */
    if (prod_id == "") {
        error_message += "Product ID must not be empty.\n";
        contains_error = true;
    }

    if (name == "") {
        error_message += "Product NAME must not be empty.\n";
        contains_error = true;
    }

    if (desc == "") {
        error_message += "Product DESCRIPTION must not be empty.\n";
        contains_error = true;
    }

    if (price == "") {
        error_message += "Product PRICING must not be empty.\n";
        contains_error = true;
    }

    if (stock == "") {
        error_message += "Product STOCK must not be empty.\n";
        contains_error = true;
    }

    if (image == "") {
        error_message += "Product IMAGE must not be empty.\n";
        contains_error = true;
    }

    // If there are any errors, throws an alert to user, else do nothing.
    if (error_message != "") {
        alert(error_message);
    }

    // Return to the calling function if validation is successful or not.
    return contains_error; 
}

function toggle_display_table() 
{
    /*
        If table is visible, hide it,
        if table is hidden, make it visible.
    */
    if (table.style.display == "none") {
        table.style.display = "table";
        table_search.style.display = "none";
        clear_search_table();
    } 
    
    else {
        /*
            If table is visible and entry is visible, do not hide table,
            if table is visible and entry is hidden, hide table.
        */
        if (entry.style.display == "none") {
            table.style.display = "none";
        }
        
        else {
            error_message = "'Entry' table must be hidden ";
            error_message += "before 'Product List' table can be hidden.";
            
            alert(error_message);
        }
    }
}

function toggle_entry_table() 
{
    // Before entry display can be displayed, `List products` must be clicked.
    if (table.style.display != "none") {
        if (!update_lock) {
            // If entry table is invisible, make it visible.
            if (entry.style.display == "none") {
                entry.style.display = "table";
            }

            else {
                entry.style.display = "none";
            }
        }

        else { // If update_lock = true
            error_msg = "Update(s) to Product id " + product_array[update_index].prod_id + " has not been completed.\n";
            error_msg += "Hide action failed.";
            alert(error_msg);
        }
    }

    else {
        alert("Please click 'List Products' first.");
    }
}

function toggle_admin_view() 
{
    if (!update_lock) {     // If update is pending, admin_view will not be able to get hidden
        if (admin_console.style.display == "none") {
        
            if (table_cart.rows.length <= 1) {
                admin_console.style.display = "block";
                cust_console.style.display = "none";

                /*
                    If admin_view button is clicked, admin_view button is disabled,
                    cust_view button is enabled.
                */
                btn_admin_view.disabled = true;
                btn_cust_view.disabled = false;
            }

            else {
                alert("Please empty cart first.");
            }
        }

        else {
            admin_console.style.display = "none";
        }
    }

    else { // update_lock = true
        var error_msg = "";

        error_msg = "Update(s) to Product id " + product_array[update_index].prod_id + " has not been completed.\n";
        error_msg += "Hide action failed.";
        alert(error_msg);
    }
}

function toggle_cust_view()
{
    if (!update_lock) {
        if (cust_console.style.display == "none") {

            cust_console.style.display = "block";
            admin_console.style.display = "none";

            /*
            If cust_view button is clicked, cust_view buton is disabled,
            admin_view button is enabled.
            */
            btn_cust_view.disabled = true;
            btn_admin_view.disabled = false;
        }

        else {
            cust_console.style.display = "none";
        }
    }

    else { // update_lock == true
        var error_msg = "";

        error_msg = "Update(s) to Product id " + product_array[update_index].prod_id + " has not been completed.\n";
        error_msg += "Delete failed.";
        alert(error_msg);
    }
}

function init() 
{
    product_array = []; // On init, empties the array
    var new_product = []; // Temporary array, for storing data to be pushed to product_array[]

    // Initial data
    new_product[0] = new product("1001", "sqli", "SQL injection", 200, 2, "img/a.png");
    new_product[1] = new product("2002", "overflow", "Buffer overflow", 250, 5, "img/b.png");
    new_product[2] = new product("3003", "lfi", "Local file include", 190, 5, "img/c.png");
    new_product[3] = new product("4004", "xss", "Cross site scripting", 65, 5, "img/z.png");
    new_product[4] = new product("5005", "upload", "File upload bug", 230, 5, "img/e.png");
    new_product[5] = new product("6006", "rat", "Remote access tool", 500, 5, "img/c.png");
    new_product[6] = new product("7007", "rce", "Remote cmd exec", 200, 6, "img/b.png");
    new_product[7] = new product("8008", "sqli", "SQL injection", 150, 3, "img/z.png");
    new_product[8] = new product("9009", "rce", "Remote cmd exec", 100, 4, "img/gravity.png");


    // Push all the array elements of new_product[] into product_array[]
    for (i = 0; i < new_product.length; i++) {
        product_array.push(new_product[i]);  
    }

    populate_table();
}

function purchase()
{
    var paypal_container = document.getElementById("paypal-button-container");
    paypal_container.style.display = 'block';

    paypal.Buttons({
        createOrder: function (data, actions) {
            // Set up the transaction
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: grand_total 
                    }
                }]
            });
        }
    }).render('#paypal-button-container');
}

var product_array = []; // The heart of the whole web app.
var cart_array = [];
var update_lock = false;  // Error checking mechanism.
var update_index; // To allow the program to know which row is currently being updated.
var grand_total;

// To allow easier access to DOM properties.
var table = document.getElementById("data");
var table_listing = document.getElementById("listing");
var table_cart = document.getElementById("cart");
var table_search = document.getElementById("search");
var entry = document.getElementById("entry");

var btn_admin_view = document.getElementById("btn_admin_view");
var btn_cust_view = document.getElementById("btn_cust_view");
var btn_update = document.getElementById("btn_update");
var btn_add = document.getElementById("btn_add");
var btn_clear = document.getElementById("btn_clear");

var admin_console = document.getElementById("admin_console");
var cust_console = document.getElementById("customer_console");

init();

/*
    On program start, update button is disabled,
    table on admin console isnt shown &
    data entry form isnt shown.
*/
btn_update.disabled = true;
table_search.style.display = "none";
table.style.display = "none";
entry.style.display = "none";

toggle_admin_view(); // Hides the admin view on startup.
btn_cust_view.disabled = true;

