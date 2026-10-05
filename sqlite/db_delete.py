import sqlite3


conn = sqlite3.connect("sandbox.db")
cur = conn.cursor()
#1 добавляем данные в таблицу
# cur.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)")
# cur.execute("INSERT INTO notes(text) VALUES('декабрь')")
# cur.execute("INSERT INTO notes(text) VALUES('ноябрь')")
# cur.execute("INSERT INTO notes(text) VALUES('март')")
# conn.commit()
# cur.execute("SELECT * FROM notes;")

#2 удаляем данные по id
# text = ''
# id = 3
# cur.execute(f"DELETE FROM notes WHERE id=?", (id,))
# conn.commit()
# # cur.execute("SELECT * FROM notes")
# notes = cur.fetchall()
# print(notes)

#3 без параметра WHERE мы полностью удаляем таблицу
cur.execute(f"DELETE FROM notes;")
conn.commit()
cur.execute("SELECT * FROM notes")
notes = cur.fetchall()
print(notes)
conn.close()