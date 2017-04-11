import pypyodbc

class MsSql(object):
    
    def __init__(self):
        self.connectionString = 'Driver={SQL Server};Server=DESKTOP-AFPM7GO;Database=MovieMonitor'

    def Insert(self, sqlCommand, values):
        connection = pypyodbc.connect(self.connectionString)  
        cursor = connection.cursor()   

        Values = values
        cursor.execute(sqlCommand,Values)   

        connection.commit()  
        connection.close()  

    def Select(self, table, columns, whereClause):
        connection = pypyodbc.connect(self.connectionString)  
        cursor = connection.cursor()   
        sqlCommand = ''
        if len(columns) == 0:
            sqlCommand = ("SELECT * FROM " + table)  
        else:
            sqlCommand = ("SELECT "+ ', '.join(str(x) for x in columns) +" FROM " + table)  


        if len(whereClause) > 0:
          sqlCommand += " " + whereClause

        cursor.execute(sqlCommand)   
        results = cursor.fetchone()   
        
        data = []
        
        while results:
            data.append(results)
            results = cursor.fetchone()  
        
        connection.close()  
        return data