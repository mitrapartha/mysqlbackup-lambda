import subprocess
import os
import time
import json

S3_BUCKET = os.environ['S3_BUCKET']

timestamp = time.strftime('%Y-%m-%d-%I:%M')


def backup(event, context):
    print("Function started")

    dbHost = os.environ['DB_HOST']
    dbName = os.environ['DB_NAME']
    dbUser = os.environ['DB_USER']
    dbPass = os.environ['DB_PASS']
# Split the variable into a list of values
#    dbName = dNames.split(',')    
    
#    print(dbHost)
    print("%s %s ".format(dbHost, dbName))
#    for idx, dbName in enumerate(dbName):
    print("Backup started for " + dbName + " database" )
#   Command to execute 
    command = "mysqldump -alv --no-tablespaces --skip-lock-tables --host %s --user %s -p%s %s | gzip > ~/%s.gz" && aws s3 cp ~/*.gz s3://%s/backup/" % (
            dbHost, dbUser, dbPass, dbName, dbName + "_" + timestamp, S3_BUCKET)
    #Execute (command)
    subprocess.Popen(command, shell=True).wait()
#        if idx < len(dbName) - 1:
    print("MySQL " + dbName + "backup finished")
    return "backup finished"
