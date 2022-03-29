#!/usr/bin/python
import logging
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
    logger.info('File open done')
    lines = data_log.readlines()
    data_log.close()
    sensor_qty = 1 
    for x in range(-sensor_qty, 0, 1):
        line = lines[x].split(',')
        logger.info(lines[x])
        location = line[0]
        logger.info(line[0])
        temp = line[1]
        logger.info(line[1])
        datum = line[4]
        logger.info(line[4])
        timeOfFile = line[5]
        logger.info(line[5])
        mycursor.execute("select time from metrics order by id desc limit 1")  
        timeOfDB = mycursor.fetchall()
        logger.info('timeOfDB ' + timeOfDB)
        if(timeOfFile != timeOfDB):
            logger.info('timeOfFile != timeOfDB -> true')
            sql = "INSERT INTO metrics (location, temp, datum, time) VALUES (%s, %s, %s, %s)"
            values = (location, temp, datum, timeOfFile)
            mycursor.execute(sql,values)
            mydb.commit();

LOG_FORMAT ="%(level)s %(asctime)s - %(messages)s"
logging.basicConfig(filename = '/home/pi/temp.log',
                        level = logging.DEBUG,
                        format = LOG_FORMAT)
logger = logging.getLogger()

#password needed to be added 
db_connect('localhost', 'root', PasswordNeeded, 'SENSORS')
write_data('/var/www/html/order.csv','r')