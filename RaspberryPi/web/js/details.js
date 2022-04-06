window.onload = function () {
    var jsonData = $.ajax ({
      url: "get_data.php?Query=4&Sensor=id",
      dataType: "json",
      async: false
    }).responseText;

    var jsonData2= $.ajax ({
        url: "get_data.php?Query=4&Sensor=datum,time",
        dataType: "json",
        async: false
    }).responseText;

    document.getElementById("chart_id").innerHTML = jsonData;
    document.getElementById("chart_time").innerHTML = jsonData2; 
}