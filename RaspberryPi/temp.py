#!/usr/bin/python
import sys
import mysql.connector

def db_connect(hostname, username, password, dbName):
    global mycursor
    global mydb
      
    mydb = mysql.connector.connect (
        host = hostname,
        user = username,
        password = password,
        database = dbName
    )
    mycursor = mydb.cursor()
    
def write_data(filepath, fileoperation):
    data_log = open(filepath, fileoperation) 
    lines = data_log.readlines()
    data_log.close()
    sensor_qty = 1 
    for x in range(-sensor_qty, 0, 1):
        line = lines[x].split(',')
        print(lines[x])
        location = line[0]
        print(line[0])
        temp = line[1]
        print(line[1])
        datum = line[4]
        print(line[4])
        timeOfFile = line[5]
        print(line[5])
        mycursor.execute("select time from metrics order by id desc limit 1")  
        timeOfDB = mycursor.fetchall()
        print(timeOfDB)
        if(timeOfFile != timeOfDB):
            sql = "INSERT INTO metrics (location, temp, datum, time) VALUES (%s, %s, %s, %s)"
            values = (location, temp, datum, timeOfFile)
            mycursor.execute(sql,values)
            mydb.commit();

#password needed to be added 
db_connect('localhost', 'root', PasswordNeeded, 'SENSORS')
write_data('/var/www/html/order.csv','r')