<?php
if(!empty($_GET["temperature"]) && !empty($_GET["humidity"]) && !empty($_GET["voltage"]) && !empty($_GET["ipsrc"])){
   $csvData = array($_GET["ipsrc"],$_GET["temperature"],$_GET["humidity"],$_GET["voltage"],date("Ymd"),date("H:i:s"));
   $fp = fopen("order.csv","a"); 
   if($fp)    {  
       fputcsv($fp,$csvData); // Write information to the file
       fclose($fp); // Close the file
   }
}
?>