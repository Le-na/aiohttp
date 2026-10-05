import sqlite3


conn = sqlite3.connect(r"hello.db") #соединение с базой данных
print("открыл соединение с БД")
conn.close()
print("закрыл соединение с БД")



