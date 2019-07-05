import sqlite3

with sqlite3.connect("ipoteca.db") as connection:

    c = connection.cursor()

    c.execute("""CREATE TABLE ipoteca (total_credit INT, total_term INT, interest_rate FLOAT)""")

