import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="")
cursor = con.cursor()
cursor.execute('use empresa')

cursor.execute("UPDATE funcionarios SET salario = 3000 WHERE nome = 'Beatriz'")

print("Salário atualizado!")
