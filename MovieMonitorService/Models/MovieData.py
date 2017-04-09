import uuid

class Movie(object):

    def __init__(self, providerID, name, description, year, rating,
                     genres, dateUploaded, torrentUrls, imageUrl):
        self.ID = uuid.uuid4()
        self.ProviderID = providerID
        self.Name = name
        self.Description = description
        self.Year = year
        self.Rating = rating
        self.Genres = genres
        self.DateUploaded = dateUploaded
        self.TorrentUrls = torrentUrls;
        self.ImageUrl = imageUrl;
