import uuid

class Torrent(object):

    def __init__(self, hash, url, size_bytes, date_uploaded, quality):
        self.ID = uuid.uuid4()
        self.ProviderHash = hash
        self.Url = url
        self.Size = size_bytes
        self.DateUploaded = date_uploaded
        self.Quality = quality


