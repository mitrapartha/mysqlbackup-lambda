import subprocess
import os
import time
import json

S3_BUCKET = os.environ['S3_BUCKET']

timestamp = time.strftime('%Y-%m-%d-%I:%M')


def backup(event, context):
    print("Function started")

    dbHost = os.environ['DB_HOST']
    dNames = os.environ['DB_NAMES']
    dbUser = os.environ['DB_USER']
    dbPass = os.environ['DB_PASS']
# Split the variable into a list of values
    dbName = dNames.split(',')    
    
#    print(dbHost)
#    print("%s %s ".format(dbHost, dbName))

    for idx, dbName in enumerate(dbName):
    # Command to execute 
        command = "mysqldump --host %s --user %s -p%s %s | gzip -c | aws s3 cp - s3://%s/%s.gz" % (
            dbHost, dbUser, dbPass, dbName, S3_BUCKET, dbName + "_" + timestamp)
    #Execute (command)
        subprocess.Popen(command, shell=True).wait()
        if idx < len(dbName) - 1:
           print("MySQL " + dbName + "backup finished")
#    return "backup finished"
