from Helpers import YifyHelper

class GetMoviesController():
    
    def StartProcess():
        YifyHelper.YifyHelper.GetLatestMovies();
        return
