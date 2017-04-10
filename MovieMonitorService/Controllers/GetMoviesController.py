from Helpers import YifyHelper
from DataControllers.MovieMonitorDB.MovieDataModel import MovieDataModel
from time import gmtime, strftime


class GetMoviesController():
    
    def StartProcess():
        yifyMovies = YifyHelper.YifyHelper.GetLatestMovies();
        entryTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        movieDataModel = MovieDataModel();

        keys = movieDataModel.Select_GetKeys();        
        keys = [ int(x) for x in keys ]

        for movie in yifyMovies:
            if any(movie.ProviderID in keys for s in keys) == False:
                movieDataModel.Insert(str(movie.ID).upper(), movie.ProviderID, movie.Name, movie.Description, movie.Year, movie.Rating, movie.DateUploaded, movie.ImageUrl, None, entryTime)
        return
