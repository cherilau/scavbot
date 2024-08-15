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


def run_sql_file(sql_file):
    # note: this is a WORKAROUND. only can run simple sql files
    conn = mysql.connector.connect(**config) 

    cursor = conn.cursor()

    with open(sql_file, encoding="utf-8") as f:
        commands = f.read().strip().split(';')

    for command in commands:
        cursor.execute(command)

    conn.commit()

    conn.close()


# a one time thing
# run_sql_file("sql/drop_tables.sql")
# run_sql_file("sql/create_tables.sql")
# run_sql_file("sql/insert_riddles.sql")
# run_sql_file("sql/insert_groups.sql")
