google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart(){
    var chartData = $.ajax({
        url: "get_data.php?Query=2",
        dataType: "json",
        async: false
    }).responseText;

    var options = {
        title: "Last 50 temperature values",
        pointSize: 10,
        titlePosition: "none",
        legend: {
            position: "none"
        }
    }

    var data = new google.visualization.DataTable(chartData);
    var chart = new google.visualization.LineChart(document.getElementById('line_chart'));

    chart.draw(data, options);
}