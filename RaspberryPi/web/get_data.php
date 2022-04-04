<?php
//echo "<h1>PHP is working fine</h1>";

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "SENSORS";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

//$sql = "SELECT id, location, temp, datum, time FROM metrics order by id desc limit 10";
$sql = 'SELECT id, temp, datum, time FROM metrics order by id desc limit 50';

$result = $conn->query($sql);

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

?>

