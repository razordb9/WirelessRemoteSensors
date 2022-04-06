google.charts.load('current', {'packages':['gauge']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var gaugeData = $.ajax({
        url: "get_data.php?Query=1&Title=Office&Sensor=temp",
        dataType: "json",
        async: false
    }).responseText;

    var options = {
        width: 400, height: 120,
        min: -20, max:50,
        greenFrom: 15, greenTo: 29,
        redFrom: 40, redTo: 50,
        yellowFrom:30, yellowTo: 40,
        minorTicks: 5
    }

    var data = new google.visualization.DataTable(gaugeData);
    var gauge = new google.visualization.Gauge(document.getElementById('gauge_div'));

    gauge.draw(data, options);
}

