import mysql.connector

conn = mysql.connector.connect(user = 'root',
                               host = 'localhost',
                               password = 'root',
                               database = 'lt2',
                               port = 8889)

print(conn)

# preparing a cursor object
cursor = conn.cursor()
 
# creating database
cursor.execute("""
              CREATE TABLE IF NOT EXISTS 
              
               """)

conn.commit()

conn.close()

