import mysql.connector

def check_if_exists(sql_statement):
    conn = mysql.connector.connect(user = 'root',
                                host = 'localhost',
                                password = 'root',
                                database = 'scav',
                                port = 8889) # hardcoded

    cursor = conn.cursor()

    cursor.execute(sql_statement)
    row = cursor.fetchone()
    if row == None:
        return False # does not exist
    else:
        return True

    conn.close()  


def return_database_results(sql_statement):
    conn = mysql.connector.connect(user = 'root',
                                host = 'localhost',
                                password = 'root',
                                database = 'scav',
                                port = 8889) # hardcoded

    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql_statement)
    result = cursor.fetchall()

    conn.close()  

    return result


def execute_sql_statement(sql_statement):
    conn = mysql.connector.connect(user = 'root',
                            host = 'localhost',
                            password = 'root',
                            database = 'scav',
                            port = 8889) # hardcoded

    cursor = conn.cursor()
    cursor.execute(sql_statement)
    conn.commit()
    conn.close()  

def run_sql_file(sql_file):
    conn = mysql.connector.connect(user = 'root',
                                host = 'localhost',
                                password = 'root',
                                database = 'scav',
                                port = 8889) # hardcoded

    cursor = conn.cursor()

    with open(sql_file, encoding="utf-8") as f:
        commands = f.read().strip().split(';')

    for command in commands:
        cursor.execute(command)
        print(command)

    conn.commit()

    conn.close()


# a one time thing
# run_sql_file("sql/drop_tables.sql")
# run_sql_file("sql/create_tables.sql")
# run_sql_file("sql/insert_riddles.sql")
# run_sql_file("sql/insert_groups.sql")