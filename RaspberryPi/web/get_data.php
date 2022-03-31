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

$sql = "SELECT id, temp, datum, time FROM metrics order by id desc limit 10";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "id: " . $row["id"]. " - Temperatur: " . $row["temp"]. " Datum: " . $row["datum"]. " Uhrzeit: " . $row["time"]. "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();

?>

