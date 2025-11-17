import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conexao.cursor()
cursor.execute("SHOW DATABASES")
cursor.execute("select * from pessoas")
for db in cursor:
    print(db)

cursor.close()
conexao.close()



