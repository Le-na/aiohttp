import sqlite3


conn = sqlite3.connect('hello.db')
cur = conn.cursor()
text = "д'Артаньян"
cur.execute("SELECT id, text FROM notes")
notes = cur.fetchall()
print(f"все записи:  {notes}")
conn.close()











