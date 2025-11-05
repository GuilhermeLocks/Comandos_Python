import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="")
cursor = con.cursor()
cursor.execute('use empresa')

cursor.execute("SELECT nome, salario FROM funcionarios ORDER BY salario DESC")

for nome, salario in cursor.fetchall():
    print(f"{nome}: R$ {salario:.2f}")
