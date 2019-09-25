<?php

$strToBeWritten = GenerateRandomString(10); // Data to be written to file.

$file = "example.txt"; // Filename to {read/write} to.

WriteToFile($file, $strToBeWritten); // Write random string to file.
ReadFromFile($file); // Read from file into webpage. 
DeleteFile($file); // Delete file from disk.

function ReadFromFile($file){
    if ($handle = fopen($file, 'r')) { // Open file for reading if there are no issues.
        // Instead of reading 1 or 2 bytes, we are going to read the whole file and store the data in a variable.
        $content = fread($handle, filesize($file));
        
        // Displays results in webpage. 
        echo "<h4>Contents of $file :</h4>"; 
        echo "<p>$content</p>"; 
        echo "<p>READ from file successful!</p><hr>";

    } else { // Issues opening file for reading.
        echo "<p>The application was not able to read from file!</p>";
    }
}

function WriteToFile($file, $strToBeWritten) {
    if ($handle = fopen($file, 'w')) { // Open file for writing and if there are no issues.

        fwrite($handle, $strToBeWritten); // Write string to the file.
        fclose($handle); // Close the file.

        echo "<p><b>String written:</b></p>"; 
        echo "<p>$strToBeWritten</p>";
        echo "<p>WRITE to file successful!</p><hr>";

    } else { // Issues opening file for writing.
        echo "<p>The application was not able to write on the file!</p>"; 
    }
}

function GenerateRandomString($length) { // Random string length.
    $chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'; // For generating random strings. 
    $charsLen = strlen($chars); // The number of characters in the variable above.

    $rand_str = 'flag {'; // Beginning of string.
    for ($i = 0; $i < $length; $i++) { // Program continues generating random string till it hits the desired string length.
        $rand_str .= $chars[rand(0,$charsLen -1)];
    }
    $rand_str .= '}'; // Tail end of string.

    return $rand_str; // Returns random string to the calling function.
}

function DeleteFile($file) {
    unlink($file); // Deletes file.
    echo "<p><b>" . strtoupper($file) . "</b> deleted succesfully!</p><hr>";
}

?>