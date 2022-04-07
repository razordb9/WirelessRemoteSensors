google.charts.load('current', {'packages':['annotationchart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart(){
    var chartData = $.ajax({
        url: "",
        dataType: "json",
        async: false
    }).responseText;

    var data = new google.visualization.DataTable(chartData);
    var chart = new google.visualization.AnnotationsChart(document.getElementById('annoChart'));

    chart.draw(data, options);
}