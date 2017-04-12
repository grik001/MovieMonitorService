import json
import requests
from Models.MovieData import Movie
from Models.TorrentData import Torrent
from Constants.YifyConstants import YifyConstants
from Helpers.ConfigSetupHelper import ConfigSetup
from Helpers.LoggerHelper import Logger

class Yify():
    """description of class"""

    def GetLatestMovies():
        Logger().Log("Retreiving MovieMetaData for Yify from {}".format(ConfigSetup.YiftMovieRequestGetUrl), "INFO")
        url = ConfigSetup.YiftMovieRequestGetUrl
        params = dict(sort_by='date_added', order_by='desc')
        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)
        
        if data['status'] != "ok":
            return None

        if data['data'] == None:
            return None
        
        movies = []

        yifyMovies = data['data']['movies']
        Logger().Log("Retreiving MovieMetaData for Yify ready : Count : {}".format(len(yifyMovies)), "INFO")
        
        for yifyMovie in yifyMovies:
            torrents = []

            for yifyTorrent in yifyMovie[YifyConstants.Torrents]:
                torrent = Torrent(yifyTorrent[YifyConstants.TorrentHash], yifyTorrent[YifyConstants.TorrentUrl], yifyTorrent[YifyConstants.TorrentSize],
                                    yifyTorrent[YifyConstants.TorrentUploadedData], yifyTorrent[YifyConstants.TorrentQuality])
                
                torrents.append(torrent);
            
            movie = Movie(yifyMovie[YifyConstants.ID], yifyMovie[YifyConstants.TitleLong], yifyMovie[YifyConstants.DescriptionFull], yifyMovie[YifyConstants.Year],
                yifyMovie[YifyConstants.Rating], yifyMovie[YifyConstants.Genres], yifyMovie[YifyConstants.DateUploaded], torrents, yifyMovie[YifyConstants.BackGroundImageOriginal])

            movies.append(movie)

        Logger().Log("Yify movie data parsed returning Count : {}".format(len(movies)), "INFO")
        return movies;

