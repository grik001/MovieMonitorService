from Controllers.GetMoviesController import GetMovies
from Controllers.GetMovieImagesController import GetMovieImages
from Helpers.ConfigSetupHelper import ConfigSetup
from Helpers.LoggerHelper import Logger

try:
    #Setup Config file to be used during Run - Settings are loaded from Config.json file
    ConfigSetup.LoadFile();
    
    #Retreieve Moves from providors & Insert in database
    GetMovies.StartProcess()

    #Review images downladed and download image bytes(cover image) if missing
    GetMovieImages.DownloadMissingImages()
except Exception as ex:
    Logger().Log("Exception occured during process: {}".format(ex), "ERROR")



