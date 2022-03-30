#!/usr/bin/python
import logging
import sys
import mysql.connector
from mysql.connector import errorcode

def db_connect(hostname, username, password, dbName):
    global mycursor
    global mydb
    
    try:
        mydb = mysql.connector.connect (
        host = hostname,
        user = username,
        password = password,
        database = dbName)
        mycursor = mydb.cursor()
        logger.info('DB connection success')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.error('Something is wrong with your user name or password')
            exit()
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.error('Database does not exist')
            exit()
        else:
            logger.error(err)
            exit() 
    
def write_data(filepath, fileoperation):
    data_log = open(filepath, fileoperation) 
    logger.info('File open done')
    lines = data_log.readlines()
    data_log.close()
    sensor_qty = 1 
    for x in range(-sensor_qty, 0, 1):
        logger.info(lines[x])
        line = lines[x].split(',')
        location = line[0]
        logger.info(line[0])
        temp = line[1]
        logger.info(line[1])
        datum = line[4]
        logger.info(line[4])
        timeOfFile = line[5]
        logger.info(line[5])
        mycursor.execute("select time from metrics order by id desc limit 1")  
        timeOfDB = mycursor.fetchone()
        timeOfFile = timeOfFile.rstrip('\n')
        logger.info('timeOfDB ' + str(timeOfDB))
        if(timeOfFile != timeOfDB[0]):
            logger.info('timeOfFile != timeOfDB -> true')
            sql = "INSERT INTO metrics (location, temp, datum, time) VALUES (%s, %s, %s, %s)"
            values = (location, temp, datum, timeOfFile)
            mycursor.execute(sql,values)
            mydb.commit();
            


if __name__ == "__main__":
    LOG_FORMAT ="%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = '/home/pi/temp.log',
                            format=LOG_FORMAT,
                            level= logging.DEBUG)
    logger = logging.getLogger()
    logger.info('########## Start Logging ##########')
    db_connect('localhost', 'root', 'yj_fb9-ePI', 'SENSORS')
    write_data('/var/www/html/order.csv','r')
    logger.info('########## Logging finished ##########')
