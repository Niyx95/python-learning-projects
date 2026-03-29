import sqlite3

#create connection and db
conn = sqlite3.connect('workout.db')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS workout (id INTEGER PRIMARY KEY AUTOINCREMENT,'
            ' date TEXT NOT NULL,'
            ' muscle_group TEXT NOT NULL,'
            ' exercise TEXT,'
            ' set_num INTEGER,'
            ' reps INTEGER,'
            ' weight_kg REAL) ')

#commit and close
conn.commit()
cur.close()
