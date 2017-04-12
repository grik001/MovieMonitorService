from Helpers.YifyHelper import Yify
from DataControllers.MovieMonitorDB.MovieDataModel import MovieDataModel
from time import gmtime, strftime
from Helpers.LoggerHelper import Logger

class GetMovies():
    
    def StartProcess():
        try:
            Logger().Log("Started Process to download movies from providers", "INFO")
        
            yifyMovies = Yify.GetLatestMovies();
            Logger().Log("Movie Meta data downloaded from providers", "INFO")
                
            entryTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            movieDataModel = MovieDataModel();

            keys = movieDataModel.Select_GetKeys();        
            keys = [ int(x) for x in keys ]
        
            Logger().Log("Starting data import to db - If movie is new", "INFO")
            for movie in yifyMovies:
                try:
                    if any(movie.ProviderID in keys for s in keys) == False:
                        Logger().Log("New Movie {} with id of {} detected inserting MetaData into Database".format(movie.Name, movie.ProviderID), "INFO")
                        movieDataModel.Insert(str(movie.ID).upper(), movie.ProviderID, movie.Name, movie.Description, movie.Year, movie.Rating, movie.DateUploaded, movie.ImageUrl, None, entryTime)
                except Exception as ex:
                    Logger().Log("Failed to save movie to database {} ex : {}".format(movie.ProviderID, ex), "ERROR")

            Logger().Log("Movie Meta data download complete", "INFO")
        except Exception as ex:
            Logger().Log("Exception occured during GetMovies process: {}".format(ex), "ERROR")

        return
