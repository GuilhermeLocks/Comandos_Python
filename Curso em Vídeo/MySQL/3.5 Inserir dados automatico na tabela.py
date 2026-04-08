import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='', database='cadastro')
cursor = con.cursor()

nome = 'naruto'
nascimento = '01-01-2000'
sexo = 'M'
altura = '1.75'
nacionalidade = 'Konora'

try:
    cursor.execute(f'''
    insert into pessoas
    (id, nome, nascimento, sexo, altura, nacionalidade)
    values
    (default, '{nome}', '{nascimento}', '{sexo}', '{altura}', '{nacionalidade}');''')

    print(f'''
insert into pessoas
(id, nome, nascimento, sexo, altura, nacionalidade)
values
(default, '{nome}', '{nascimento}', '{sexo}', '{altura}', '{nacionalidade}');''')
    print('\nDados inseridos com sucesso!\n')

except Exception as Erro:

    print(f'Erro: {Erro}')

nome = 'sasuke'
nascimento = '01-01-2000'
sexo = 'M'
altura = '1.75'
nacionalidade = 'Konora'

try:
    cursor.execute(f'''
    insert into pessoas
    (id, nome, nascimento, sexo, altura, nacionalidade)
    values
    (default, '{nome}', '{nascimento}', '{sexo}', '{altura}', '{nacionalidade}');''')

    print(f'''
insert into pessoas
(id, nome, nascimento, sexo, altura, nacionalidade)
values
(default, '{nome}', '{nascimento}', '{sexo}', '{altura}', '{nacionalidade}');''')
    print('\nDados inseridos com sucesso!\n')

except Exception as Erro:

    print(f'Erro: {Erro}')

nome = 'Python'
descricao = 'Curso'
carga = '120'
totaulas = '80'
ano = '2026'

try:
    cursor.execute(f'''
insert into cursos
(nome, descricao, carga, totaulas, ano)
values
('{nome}', '{descricao}', '{carga}', '{totaulas}', '{ano}');''')

    print(f'''
insert into cursos
(nome, descricao, carga, totaulas, ano)
values
('{nome}', '{descricao}', '{carga}', '{totaulas}', '{ano}');''')
    print('\nDados inseridos com sucesso!')

except Exception as Erro:

    print(f'Erro: {Erro}')

nome = 'Java'
descricao = 'Curso'
carga = '80'
totaulas = '30'
ano = '2015'

try:
    cursor.execute(f'''
insert into cursos
(nome, descricao, carga, totaulas, ano)
values
('{nome}', '{descricao}', '{carga}', '{totaulas}', '{ano}');''')

    print(f'''
insert into cursos
(nome, descricao, carga, totaulas, ano)
values
('{nome}', '{descricao}', '{carga}', '{totaulas}', '{ano}');''')
    print('\nDados inseridos com sucesso!')

except Exception as Erro:

    print(f'Erro: {Erro}')