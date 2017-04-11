from Helpers.MsSqlHelper import MsSql
import mock
import uuid

class MovieDataModel():
    
    def __init__(self):
        pass

    def Insert(self, id ,providerID ,name ,description ,year ,rating ,dateUploaded ,imageUrl ,imageBytes, entryTime):
        MsSql().Insert("INSERT INTO Movie([ID], [EntryTime],[ProviderID] ,[Name] ,[Description] ,[Year] ,[Rating] ,[DateUploaded] ,[ImageUrl] ,[ImageBytes])" + "VALUES(?,?,?,?,?,?,?,?,?,?)",
        [id, entryTime, providerID ,name ,description ,year ,rating ,dateUploaded ,imageUrl ,imageBytes])

    def Select_GetKeys(self):
        data = MsSql().Select("Movie", ["CAST(ID AS VARCHAR(36)) ID", "ProviderID"], "");
        movies = []

        for val in data:
            movie = val[1]    
            movies.append(movie)

        return movies;

    def Select_GetMoviesMissingImages(self):
        data = MsSql().Select("Movie", ["CAST(ID AS VARCHAR(36)) ID", "ImageUrl"], "WHERE ImageBytes IS NULL");
        movies = []
        
        for val in data:
            movie = mock.Mock()
            movie.ID = val[0]
            movie.ImageUrl = val[1]    
            movies.append(movie)
        
        return movies;

    def UpdateImageBytes(self, movie):
        data = MsSql().Insert("UPDATE Movie SET ImageBytes = ? WHERE ID = ? ", [movie.ImageBytes, movie.ID])
        return
        