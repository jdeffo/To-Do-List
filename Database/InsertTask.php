<?php

  include()'dbConfig.php');

  $sqlTest = "SELECT * FROM tasks";

  $santitle = mysqli_real_escape_string($conn, _POST['title']);
  $sanduedate = mysqli_real_escape_string($conn, _POST['du_date']);
  $sanstatus = mysqli_real_escape_string($conn, _POST['status']);

  $sql = "INSERT INTO task(title, due_date, status) VALUES('$santitle', '$sanduedate', '$sanstatus')";

  $result = mysqli_query($conn, $sqlTest);

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
