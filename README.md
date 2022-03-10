# WirelessRemoteSensors
The idea behind this is to combine several technics within project.
We will use several sensors to gather the temperature within my living space.

Hardware:
Wemos D1 mini pro
DS18S20 or DHT22
Raspberry Pi b+
Synology DS418play

With the Wemos D1 mini pro I will measure the temperature from the sensor. A Raspberry Pi b+ will collect the data from the Wemos and write it into a MySQL database. To visualize the data we will create a simple webpage to display the data for every sensor. 

Wemos Documentation: https://www.wemos.cc/en/latest/index.html#