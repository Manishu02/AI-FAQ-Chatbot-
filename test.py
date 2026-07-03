import sqlite3

conn = sqlite3.connect("faq.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM faq")

print(cursor.fetchall())

conn.close()