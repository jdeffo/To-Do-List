<?php

include dbConfig.php;

$sql = "SELECT * FROM tasks";

$result = mysqli_query($conn, $sql);

mysqli_close($conn);

 ?>
