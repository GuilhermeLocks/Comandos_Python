import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="")
cursor = con.cursor()
cursor.execute('use empresa')

cursor.execute("SELECT * FROM funcionarios WHERE nome = 'Carlos'")

print(cursor.fetchone())
