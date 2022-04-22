#!/bin/bash
#
# bkp_mysql.sh 1.0
#
#
# Dumps all databases to a seperate file
# All files are created in a folder named the current date
# Folders exceeding the defined hold time are purged automatically
#
# (c) 2022 Thomas Zaußnig
#

HOLD_DAYS=7
TIMESTAMP=$(date +"%F")
BACKUP_DIR="/bkp/MySQL"

MYSQL_USR="root"
MYSQL_PWD="PWD"

MYSQL_CMD=/usr/bin/mysql
MYSQL_DMP=/usr/bin/mysqldump
MYSQL_CHECK=/usr/bin/mysqlcheck

#Check and auto repair all databases
echo
echo "Checking all databases - this can take a while..."
$MYSQL_CHECK -u $MYSQL_USR --password=$MYSQL_PWD --auto-repair --all-databases

#Backup
echo "Starting backup..."
mkdir -p "$BACKUP_DIR/$TIMESTAMP"
$MYSQL_DMP -u $MYSQL_USR -p$MYSQL_PWD --all-databases > gzip > "$BACKUP_DIR/$TIMESTAMP/file.sql"
databases=`$MYSQL_CMD --user=$MYSQL_USR -p$MYSQL_PWD -e "SHOW DATABASES;" | grep -Ev "(Database|information_schema|performance_schema)"`

for db in $databases; do
	echo "Dumbing $db..."
	$MYSQL_DMP --force --opt --user=$MYSQL_USR -p$MYSQL_PWD --databases "$db" | gzip > "$BACKUP_DIR/$TIMESTAMP/$db.gz"
done

#Clean up
echo
echo "Cleaning up..."
find $BACKUP_DIR -type d -mtime +$HOLD_DAYS -maxdepth 1 -mindepth 1 -exec rm -rf {} \;
echo "Backup done!"
