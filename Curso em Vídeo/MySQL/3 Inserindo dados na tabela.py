import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='', database='naruto')
cursor = con.cursor()

nome = str(input('Nome: '))
nascimento = str(input('Data de nascimento: '))
sexo = str(input('Sexo: '))
altura = str(input('Altura: '))
nacionalidade = str(input('Nacionalidade: '))

try:
    cursor.execute(f'''
    insert into pessoas
    (id, nome, nascimento, sexo, altura, nacionalidade)
    values
    (default, '{nome}', '{nascimento}', '{sexo}', '{altura}', '{nacionalidade}');''')

    print('Dados inseridos com sucesso!')

except Exception as Erro:

    print(f'Erro: {Erro}')