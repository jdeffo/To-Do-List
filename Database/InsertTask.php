<?php

  include dbConfig.php;

  $sql = "SELECT * FROM tasks";
  $result = mysqli_query($conn, $sql);

  if (mysqli_num_rows($result) > 0) {
    echo "<table border='1'>
    <tr>
    <th>TID</th>
    <th>Title</th>
    <th>Due Date</th>
    <th>Status</th>";
    while($row = mysqli_fetch_assoc($result)) {
      echo "<tr>";
      echo "<td>" . $row["tid"] . "</td>" . "<td>" . $row["title"] . "</td><td>" . $row["due_date"] . "</td><td>" . $row["status"] . "</td>";
      "</tr>";
    }
    echo "</table";

  }

  mysqli_close($conn);

 ?>
