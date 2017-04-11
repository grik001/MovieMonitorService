import urllib
import requests
import shutil
from io import StringIO
from DataControllers.MovieMonitorDB.MovieDataModel import MovieDataModel

class GetMovieImages():
    
    def DownloadMissingImages():

        movies = MovieDataModel().Select_GetMoviesMissingImages();        
        
        for movie in movies:
            response = requests.get(movie.ImageUrl)
            bytes = bytearray(response.content)
            movie.ImageBytes = bytes;
            MovieDataModel().UpdateImageBytes(movie);

        return
