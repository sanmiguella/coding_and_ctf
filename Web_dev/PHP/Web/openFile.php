<?php

$strToBeWritten = "Let's see how deep the rabbit hole goes!"; // Data to be written to file.
$file = "example.txt"; // Filename.

WriteToFile($file, $strToBeWritten);
echo "<hr>";
ReadFromFile($file); 

function ReadFromFile($file){
    if ($handle = fopen($file, 'r')) { // Open file for reading if there are no issues.
        // Instead of reading 1 or 2 bytes, we are going to read the whole file and store the data in a variable.
        $content = fread($handle, filesize($file));
        
        // Displays results in webpage. 
        echo "<h4>Contents of $file</h4>"; 
        echo "<p>$content</p>"; 

    } else { // Issues opening file for reading.
        echo "<p>The application was not able to read from file</p>";
    }
}

function WriteToFile($file, $strToBeWritten) {
    if ($handle = fopen($file, 'w')) { // Open file for writing and if there are no issues.
        echo "<h4>Opening $file for writing</h4>";

        fwrite($handle, $strToBeWritten); // Write string to the file.
        fclose($handle); // Close the file.

        echo "<p><b>String written:</b></p>"; 
        echo "<p>$strToBeWritten</p>";
    
    } else { // Issues opening file for writing.
        echo "<p>The application was not able to write on the file!</p>"; 
    }
}

?>