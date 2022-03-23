#!/usr/bin/python
import MySQLdb
import sys

def db_connect():
    global cur
    global con
    con = MySQLdb.connect(host="localhost", user="root", password="")
    cur = con.cursor()
    cur.execute("USE SENSORS;")

def write_data():
    data_log = open('/var/www/html/order.csv','r') 
    lines = data_log.readlines()
    data_log.close()
    sensor_qty = 1 
    for x in range(-sensor_qty, 0, 1):
        line = lines[x].split(',')
        print(lines[x])
        v1 = line[0]
        print(line[0])
        v2 = line[1]
        print(line[1])
        v3 = line[4]
        print(line[4])
        v4 = line[5]
        print(line[5])
        cur.execute("INSERT INTO metrics (location, temp, datum, time) VALUES (%s, %s, %s, %s)", (v1, v2, v3, v4))
        con.commit();
        
db_connect()
write_data()