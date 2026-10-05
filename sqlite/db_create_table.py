import sqlite3


conn = sqlite3.connect(r"hello.db") #соединение с базой данных
print("открыл соединение с БД")
cur = conn.cursor() #позволяет делать sql-запросы к БД. cur - хранит этот объект и его мы используем в жальнейшем
cur.execute("""CREATE TABLE IF NOT EXISTS notes(
id INTEGER PRIMARY KEY,
text TEXT);
""")  #выполняем различные запросы к БД
conn.commit()   #
conn.close()    #
print("закрыл соединение с БД")



