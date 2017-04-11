import json
import requests
from Models.MovieData import Movie
from Models.TorrentData import Torrent
from Constants.YifyConstants import YifyConstants
from Helpers.ConfigSetupHelper import ConfigSetup

class Yify():
    """description of class"""

    def GetLatestMovies():
        url = ConfigSetup.YiftMovieRequestGetUrl
        params = dict(sort_by='date_added', order_by='desc')
        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)
        
        if data['status'] != "ok":
            return None

        if data['data'] == None:
            return None
        
        movies = []
        
        for val in data['data']['movies']:

            torrents = []
            for yifyTorrent in val[YifyConstants.Torrents]:
                torrent = Torrent(yifyTorrent[YifyConstants.TorrentHash], yifyTorrent[YifyConstants.TorrentUrl], yifyTorrent[YifyConstants.TorrentSize],
                                    yifyTorrent[YifyConstants.TorrentUploadedData], yifyTorrent[YifyConstants.TorrentQuality])
                
                torrents.append(torrent);
            
            movie = Movie(val[YifyConstants.ID], val[YifyConstants.TitleLong], val[YifyConstants.DescriptionFull], val[YifyConstants.Year],
                val[YifyConstants.Rating], val[YifyConstants.Genres], val[YifyConstants.DateUploaded], torrents, val[YifyConstants.BackGroundImageOriginal])

            movies.append(movie)
        return movies;

