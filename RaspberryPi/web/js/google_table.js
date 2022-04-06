google.charts.load('current', {'packages':['table']});
google.charts.setOnLoadCallback(drawTable);

function drawTable(){
    var tableData = $.ajax({
        url: "get_data.php?Query=3&Title=Office&Sensor=min(temp),max(temp)",
        dataType: "json",
        async: false
    }).responseText;

    var options ={
        width: '100%'
    }

    var data = new google.visualization.DataTable(tableData);
    var table = new google.visualization.Table(document.getElementById('chart_table'));

    table.draw(data, options)
}