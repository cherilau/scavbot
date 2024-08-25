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
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql_statement)
    result = cursor.fetchone()
    conn.close()
    return result

def fetch_many(sql_statement):
    conn = mysql.connector.connect(**config)
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql_statement)
    result = cursor.fetchall()

    conn.close()  

    return result


def execute_sql_statement(sql_statement):
    conn = mysql.connector.connect(**config)

    cursor = conn.cursor()
    cursor.execute(sql_statement)
    conn.commit()
    conn.close()  

