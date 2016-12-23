<?php

  include dbConfig.php;

  $santid = mysqli_real_escape_string($conn, _POST['tid']);
  //$santitle = mysqli_real_escape_string($conn, _POST['title']);
  //$sanduedate = mysqli_real_escape_string($conn, _POST['du_date']);
  //$sanstatus = mysqli_real_escape_string($conn, _POST['status']);

//Select the task to complete
  $sqlSelect = "SELECT * FROM task";
  $selectResult = mysqli_query($conn, $sqlSelect);
  $row = mysqli_fetch_assoc($result)
  $santitle = $row['title'];
  $sanduedate = $row['due_date'];
  $sanstatus = $row['status'];

  $sqlRemove = "DELETE FROM task WHERE task.tid = '$santid'";

  $sqlComplete = "INSERT INTO completed(tid, title, due_date, status) VALUES('$santid', '$santitle', '$sanduedate', '$sanstatus')";

 ?>
