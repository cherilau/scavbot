import mysql.connector

config = {
    "user": "root",
    "host": "localhost",
    "password": "root",
    "database": "scav",
    "port": 8889,
    "host": "127.0.0.1"
}

def fetch_one(sql_statement):
    conn = mysql.connector.connect(**config) # hardcoded
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql_statement)
    result = cursor.fetchone()
    conn.close()
    return result

# result = fetch_one("select * from user where username = 'no';")
print(result)
