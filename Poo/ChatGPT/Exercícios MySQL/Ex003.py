import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="")
cursor = con.cursor()
cursor.execute('use empresa')

sql = "INSERT INTO funcionarios (nome, cargo, salario) VALUES (%s, %s, %s)"
dados = [
    ("Ana", "Gerente", 7500),
    ("Carlos", "Analista", 4500),
    ("Beatriz", "Assistente", 3000)
]
cursor.executemany(sql, dados)

print("Dados inseridos!")
