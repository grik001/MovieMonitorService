import urllib
import requests
import shutil
from io import StringIO
from DataControllers.MovieMonitorDB.MovieDataModel import MovieDataModel
from Helpers.LoggerHelper import Logger

class GetMovieImages():
    
    def DownloadMissingImages():
        try:
            Logger().Log("Started Process to download missing cover image for movie meta data", "INFO")
            movies = MovieDataModel().Select_GetMoviesMissingImages();        
            
            Logger().Log("Total movies missing image : {}".format(len(movies)), "INFO")

            for movie in movies:
                try:
                    Logger().Log("Starting image download from : {} for movie {}".format(movie.ImageUrl, movie.ID), "INFO")
                    response = requests.get(movie.ImageUrl)
                    if len(response.content) > 0:
                        Logger().Log("Image downloaded sucessfully for : {}".format(movie.ID), "INFO")
                        bytes = bytearray(response.content)
                        movie.ImageBytes = bytes;
                        MovieDataModel().UpdateImageBytes(movie);
                    else:
                        Logger().Log("No content found for image in response - image not saved for : {}".format(movie.ID), "INFO")
                except Exception as ex:
                    Logger().Log("Exception occured during downloading/parsing of image {} : ex {}".format(movie.ID, ex), "ERROR")

            Logger().Log("Image download process complete", "INFO")
        except Exception as ex:
            Logger().Log("Exception occured during GetMovieImages process: {}".format(ex), "ERROR")
        return
