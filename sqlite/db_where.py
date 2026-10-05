import sqlite3


conn = sqlite3.connect('hello.db')
cur = conn.cursor()
text = "д'Артаньян"
cur.execute("SELECT id, text FROM notes WHERE text = ?", (text,))
notes = cur.fetchall()
print(f"где текст = {text} принт:  {notes}")
date= "октябрь"
cur.execute("SELECT id, text FROM notes WHERE text = ?", (date,))
row = cur.fetchall()
print(f"где текст = {date} принт:  {row}")
conn.close()




