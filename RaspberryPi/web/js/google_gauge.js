google.charts.load('current', {'packages':['gauge']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var gaugeData = $.ajax({
        url: "get_data.php",
        dataType: "json",
        async: false
    }).responseText;

    var options = {
        width: 400, height: 120,
        redFrom: 90, redTo: 100,
        yellowFrom:75, yellowTo: 90,
        minorTicks: 5
    }

    var data = new google.visualization.DataTable(gaugeData);
    var gauge = new google.visualization.Gauge(document.getElementById('gauge_div'));

    gauge.draw(data, options);
}

