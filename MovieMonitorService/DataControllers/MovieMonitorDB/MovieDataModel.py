from Helpers.MsSqlHelper import MsSqlHelper

class MovieDataModel():
    
    def __init__(self):
        pass

    def Insert(self, id ,providerID ,name ,description ,year ,rating ,dateUploaded ,imageUrl ,imageBytes, entryTime):
        MsSqlHelper().Insert("INSERT INTO Movie([ID], [EntryTime],[ProviderID] ,[Name] ,[Description] ,[Year] ,[Rating] ,[DateUploaded] ,[ImageUrl] ,[ImageBytes])" + "VALUES(?,?,?,?,?,?,?,?,?,?)",
        [id, entryTime, providerID ,name ,description ,year ,rating ,dateUploaded ,imageUrl ,imageBytes])

    def Select_GetKeys(self):
        data = MsSqlHelper().Select("Movie", ["ID", "ProviderID"]);
        movies = []

        for val in data:
            movie = val[1]    
            movies.append(movie)

        return movies;
        