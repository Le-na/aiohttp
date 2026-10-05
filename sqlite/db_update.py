import sqlite3




conn = sqlite3.connect('hello.db')
cur = conn.cursor()
cur.execute("SELECT * FROM notes;")
notes = cur.fetchall()
print(notes)
text = 'обновленная запись'
id = 2
cur.execute(f"UPDATE notes SET text=? WHERE id=?;", (text, 2))
conn.commit()
cur.execute("SELECT * FROM notes;")
n = cur.fetchall()
print(n)
conn.close()
