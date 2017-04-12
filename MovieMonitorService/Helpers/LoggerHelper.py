from pymongo import MongoClient
from Helpers.ConfigSetupHelper import ConfigSetup
from datetime import datetime

class Logger():
    
    def __init__(self):
        pass

    def Log(self, message, type):
        client = MongoClient(ConfigSetup.LoggingMongoConnectionString)
        db = client.LoggingDB
        logsTable = db.Logs
        log = {"EntryTime": datetime.utcnow(), "System": "MovieMonitor", "LogType" : type, "Message" : message}
        logsTable.insert_one(log)
        pass