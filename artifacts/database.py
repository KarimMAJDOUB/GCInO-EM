from configparser import ConfigParser
import os 
import pymysql.connections as MySQLdb

class Database:
    def __init__(self):
        # Fetch configuration Data
        # Read config.ini file
        config_object = ConfigParser()
        self.path_to_config = os.path.dirname(os.path.dirname(__file__)) + "\system_files\config.ini"
        config_object.read(self.path_to_config)

        # Get the password
        databaseInfo = config_object["DATABASECONFIG"]

        self.DB_SERVER = databaseInfo["DB_SERVER"]
        self.DB_USERNAME = databaseInfo["DB_USERNAME"]
        self.DB_PASSWORD = databaseInfo["DB_PASSWORD"]
        self.DB_NAME = databaseInfo["DB_NAME"]