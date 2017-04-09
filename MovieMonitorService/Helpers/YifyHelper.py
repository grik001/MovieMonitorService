import json
import requests
from Models import MovieData
from Constants.YifyConstants import YifyConstants

class YifyHelper():
    """description of class"""

    def GetLatestMovies():
        url = 'https://yts.ag/api/v2/list_movies.json'
        params = dict(sort_by='date_added', order_by='desc')
        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)
        
        if data['status'] != "ok":
            return None

        if data['data'] == None:
            return None
        
        movies = []

        for val in data['data']['movies']:
            movie = MovieData.Movie(val[YifyConstants.ID], val[YifyConstants.TitleLong], val[YifyConstants.DescriptionFull], val[YifyConstants.Year],
                val[YifyConstants.Rating], val[YifyConstants.Genres], val[YifyConstants.DateUploaded], val[YifyConstants.Torrents], val[YifyConstants.BackGroundImageOriginal])

            movies.append(movie)
            
        return

