import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="")
cursor = con.cursor()
cursor.execute('use empresa')

cursor.execute("SELECT COUNT(*) FROM funcionarios")

qtd = cursor.fetchone()[0]
print(f"Total de funcionários: {qtd}")
