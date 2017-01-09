<!--Connecting to the database-->

<?php

$servername = 'localhost';
$username = 'root';
$password = 'Wildcats5966';
$database = 'tododb';
$conn = mysqli_connect($servername, $username, $password, $database);

if(mysqli_connect_errno()) {

echo nl2br("Failed to connect to MySQL:" .mysqli_connect_error(). "\n");

}
else {
echo nl2br("Established Database Connection \n");
}


 ?>
