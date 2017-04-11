from Controllers.GetMoviesController import GetMovies
from Controllers.GetMovieImagesController import GetMovieImages

from Helpers.ConfigSetupHelper import ConfigSetup
import json

ConfigSetup.LoadFile();
GetMovies.StartProcess()
GetMovieImages.DownloadMissingImages()



