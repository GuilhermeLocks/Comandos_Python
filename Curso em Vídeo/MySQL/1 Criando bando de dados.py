import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='')
cursor = con.cursor()

try:
    cursor.execute('''CREATE DATABASE IF NOT EXISTS naruto
    default character set utf8
    default collate utf8_general_ci
    ''')
    print("Banco de dados criado com sucesso!")
except:
    print("Erro ao criar banco de dados.")