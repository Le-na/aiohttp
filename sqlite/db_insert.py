import sqlite3



conn = sqlite3.connect('hello.db')
cur = conn.cursor()
cur.execute("INSERT INTO notes(text) VALUES('третья запись')")
conn.commit()
conn.close()