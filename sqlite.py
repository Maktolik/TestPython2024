import sqlite3

DB_NAME = "sqlite3_db.db"


with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """SELECT * FROM users"""
    sql_cursor = sqlite_conn.execute(sql_request)
    for row in sql_cursor:
        print(row)





# users = [
#     (1, 'Egor', 'egor@mail.com', '123456'),
#     (22, 'Elena', 'elena@mail.com', '123456'),
#     (33, 'Ezik', 'ezik@mail.com', '123456'),
#     (44, 'Tolik', 'makarenko@mail.com', '123456'),
# ]
#
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """INSERT INTO users VALUES(?, ?, ?, ?)"""
#     for user in users:
#         sqlite_conn.execute(sql_request, user)
#     sqlite_conn.commit()
#
#

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS users (
#     id integer PRIMARY KEY,
#     name text NOT NULL,
#     email text NOT NULL,
#     password text NOT NULL
#     );"""
#     sqlite_conn.execute(sql_request)