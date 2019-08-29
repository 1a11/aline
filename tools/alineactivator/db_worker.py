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
                  (skey text,  rkey text)
               """)
        cursor.execute("""CREATE TABLE api
                  (key text)""")
        
    #--<
    """
        Get colum values
        
        get_settings(channel) - will get values from table settings where channel is channel name
            channel - type: string,  example: '#abcdef'
    """       
    def get_settings(self,  owner_id):
        sql = "SELECT * FROM settings WHERE skey=?"
        cursor.execute(sql,  [(owner_id)])
        return cursor.fetchall()
    def get_apikey(self,  owner_id):
        sql = "SELECT * FROM api WHERE key=?"
        cursor.execute(sql,  [(owner_id)])
        return cursor.fetchall()
    
    #--<
    def create_settings(self, values):
        sql = """
        INSERT INTO settings
        VALUES ('{}', '{}')
        """.format(values['skey'], values['rkey'])
        cursor.execute(sql)
        conn.commit()
    def create_apikey(self, key):
        sql = """
        INSERT INTO api
        VALUES ("{}")
        """.format(key)
        cursor.execute(sql)
        conn.commit()
        
##db = database('prod.db')
##db.create()
##skeys = []
##rkeys = []
##akeys = []
##for i in range(10):
##    skey = str(uuid.uuid4())
##    rkey = str(uuid.uuid4())
##    skeys.append(skey)
##    rkeys.append(rkey)
##    db.create_settings({'skey':skey,'rkey':rkey})
##for i in range(4):
##    akey = str(uuid.uuid4())
##    akeys.append(akey)
##    db.create_apikey(akey)
##print('-SKEYS-')
##i2=0
##for i in skeys:
##    print(i2,'-',i)
##    i2+=1
##print()
##i2=0
##print('-RKEYS-')
##for i in rkeys:
##    print(i2,'-',i)
##    i2+=1
##print('-AKEYS-') 
##for i in akeys:
##    print(i)
