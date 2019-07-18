import sqlite3


class database():
    def __init__(self,  dbname):
        try:
            global conn
            conn = sqlite3.connect(dbname)
            global cursor
            cursor = conn.cursor()
        except Exception as exc:
            raise Exception(exc)
    #--<
    """
        If your database was f***ed up by something,  you can create new one

        create() - will create a new tables in your database
    """
    def create(self):
        cursor.execute("""CREATE TABLE settings
                  (owner_id int,  token text,  user_token text)
               """)
        
    #--<
    """
        Get colum values
        
        get_settings(channel) - will get values from table settings where channel is channel name
            channel - type: string,  example: '#abcdef'
    """       
    def get_settings(self,  owner_id):
        sql = "SELECT * FROM settings WHERE owner_id=?"
        cursor.execute(sql,  [(owner_id)])
        return cursor.fetchall()
    
    #--<
    def create_settings(self,  owner_id,  values):
        sql = """
        INSERT INTO settings
        VALUES ('{}', '{}', '{}')
        """.format(owner_id, values['token'], values['user_token'])
        print(sql)
        cursor.execute(sql)
        conn.commit()
        
