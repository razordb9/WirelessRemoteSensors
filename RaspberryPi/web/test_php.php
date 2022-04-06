<?php
//echo "<h1>PHP is working fine</h1>";

$servername = "localhost";
$username = "root";
$password = "yj_fb9-ePI";
$dbname = "SENSORS";

$query = $_GET["Query"];
$title = $_GET["Title"];

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
;
switch ($query) {
  case "1":
    $sql_query = "Select temp from metrics order by id desc limit 1;";
    wrgauge();
    break;
  case "2":
    $sql_query = "Select id, temp, datum, time from (select id, temp, datum, time from metrics order by id desc limit 50) sub order by id asc;";
    wrlinechart();
    break;
  default:
    print "Wrong query parameter";
}

function wrgauge() {
  global $sql_query;
  global $conn;
  global $title;

  $result = $conn->query($sql_query);

  $rows = array();
  $table = array();


  $table['cols'] = array(
    array('label' => 'String', 'type' => 'string'),
    array('label' => 'Value', 'type' => 'number'),
  );

  while($row = $result->fetch_assoc()) {
    $sub_array = array();
    $sub_array[] = array('v' => $title);
    $sub_array[] = array('v' => $row['temp']);
    $rows[] = array('c' => $sub_array);
  }

  $table['rows'] = $rows;
  $jsonTable = json_encode($table);
  echo $jsonTable;

}

function wrlinechart() {
  global $sql_query;
  global $conn;
  global $title;
  
  $result = $conn->query($sql_query);

  $rows = array();
  $table = array();
  
  
  $table['cols'] = array(
    array('label' => 'Date time', 'type' => 'string'),
    array('label' => 'Temperatur', 'type' => 'number'),
  );
  
  while($row = $result->fetch_assoc()) {
    $sub_array = array();
    $sub_array[] = array('v' => $row['datum'] . ' ' . $row['time']);
    $sub_array[] = array('v' => $row['temp']);
    $rows[] = array('c' => $sub_array);
  }
  
  $table['rows'] = $rows;
  $jsonTable = json_encode($table);
  echo $jsonTable;
}





?>