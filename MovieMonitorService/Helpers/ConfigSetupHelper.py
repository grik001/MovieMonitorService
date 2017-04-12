import json, sys, codecs

class ConfigSetup():
    
        YiftMovieRequestGetUrl = ""
        MoviesDatabaseConnectionString = ""
        LoggingMongoConnectionString = ""

        @staticmethod
        def LoadFile():
           with open('Config.json', encoding='utf-8-sig') as json_file:  
                data = json.load(json_file)
                ConfigSetup.YiftMovieRequestGetUrl = data["YiftMovieRequestGetUrl"]
                ConfigSetup.MoviesDatabaseConnectionString = data["MoviesDatabaseConnectionString"]
                ConfigSetup.LoggingMongoConnectionString = data["LoggingMongoConnectionString"]
        
