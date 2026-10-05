import sqlite3


conn = sqlite3.connect('hello.db')
cur = conn.cursor()
text = "д'Артаньян"
# cur.execute("INSERT INTO notes(text) VALUES(?)", (text,))
# conn.commit()
cur.execute("SELECT * FROM notes")
notes = cur.fetchall()
print(notes)
conn.close()