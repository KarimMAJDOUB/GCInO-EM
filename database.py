from configparser import ConfigParser
import os 
import pymysql.connections as MySQLdb

class Database:
    def __init__(self):
        # Fetch configuration Data
        # Read config.ini file
        config_object = ConfigParser()
        config_object.read("config.ini")

        # Get the password
        databaseInfo = config_object["DATABASECONFIG"]

        self.DB_SERVER = databaseInfo["DB_SERVER"]
        self.DB_USERNAME = databaseInfo["DB_USERNAME"]
        self.DB_PASSWORD = databaseInfo["DB_PASSWORD"]
        self.DB_NAME = databaseInfo["DB_NAME"]

        self.conn = MySQLdb.Connection(host= self.DB_SERVER,
                                     user = self.DB_USERNAME,
                                     password= self.DB_PASSWORD, 
                                     database= self.DB_NAME
                                    )
    
    def connectToDB(self):
        """
        """
        return self.conn
        
    def executeQuery(self, query, fetch ='one'):
        """
        """
        cursor = self.conn.cursor()
        cursor.execute(query)
        if fetch =='one':
            data = cursor.fetchone()
        else:
            data = cursor.fetchall()
        return data

