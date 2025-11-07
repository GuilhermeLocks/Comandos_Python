import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="")
cursor = con.cursor()
cursor.execute('use empresa')

cursor.execute("SELECT AVG(salario) FROM funcionarios")

media = cursor.fetchone()[0]
print(f"Média salarial: {media:.2f}")
