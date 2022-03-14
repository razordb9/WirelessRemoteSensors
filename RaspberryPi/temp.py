#!/usr/bin/python
data_log = open('/var/www/html/order.csv','r') 
lines = data_log.readlines()
data_log.close()
 
sensor_qty = 3     # how many sensor lines to read in from log
 
html_string = '<html>\n<body>\n<style>\ntable { \n  border-spacing: 10px;\n'
html_string += '  border-collapse: separate;\n}\n</style>\n'
html_string += '\n<table>\n<tr align="center">\n<th>Location</th>'
html_string += '<th>Temp</th><th>Date</th><th>Time</th></tr>\n'
 
for x in range(-sensor_qty, 0, 1):
    line = lines[x].split(',')
 
    html_string += '<tr><td align="right">'
    html_string += line[0]
    html_string += '</td><td align="right">'
    html_string += line[1]
    html_string += '&deg;C </td><td>'
    html_string += line[4]
    html_string += '</td><td> '
    html_string += line[5]
    html_string += '</td></tr>\n'
 
html_string += '</table>\n\n</body>\n</html>'
 
html_file = open('/var/www/html/temps.html','w') 
html_file.write(html_string)
html_file.close()