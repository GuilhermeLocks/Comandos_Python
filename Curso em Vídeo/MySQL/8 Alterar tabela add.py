import mysql.connector
import os
con = mysql.connector.connect(host='localhost', user='root', password='', database='cadastro')
cursor = con.cursor()


while True:
    while True:
        try:

            comando = int(input('''\n1 Adiciona coluna profissão
2 Adicinada coluna profissão depois de nome
3 Adicinada coluna profissão em primeiro lugar
4 Modificada coluna profissão
5 Renomeada coluna profissão para prof
6 Deletar coluna prof
7 Adicionado idcurso em primeiro lugar
8 Alterado idcurso para chave primaria
9 removando idcurso como chave primaria
10 renomea database para curso
11 renomea database para cursos
12 adiciona coluna ninja
13 altera coluna ninja para cheve estrageira 
14 adiciona o itachi

Digite um numero entre 1 a 14:'''))
        except:
            print('Comando invalido tente novamente!')
        if comando >= 1 and comando <= 14:
            break
        else:
            print('Comando invalido tente novamente')

    os.system('cls')

    if comando == 1:
        try:
            cursor.execute('''alter table pessoas
                              add column profissao varchar(10);''')
            print('''alter table pessoas
add column profissao varchar(10);''')

        except Exception as erro:
            print(f'Erro: {erro}')
    if comando == 2:
        try:
            cursor.execute('''alter table pessoas
                           add column profissao varchar(10) after nome;''')
            print('''alter table pessoas
add column profissao varchar(10) after nome;''')

        except Exception as erro:
            print(f'Erro: {erro}')
    if comando == 3:
        try:
            cursor.execute('''alter table pessoas
                           add column profissao varchar(10) first;''')
            print('''alter table pessoas
add column profissao varchar(10) first;''')

        except Exception as erro:
            print(f'Erro: {erro}')
    if comando == 4:
        try:
            cursor.execute('''alter table pessoas
                           modify column profissao varchar(20) not null;''')
            print('''alter table pessoas
modify column profissao varchar(20) not null;''')

        except Exception as erro:
            print(f'Erro: {erro}')
    if comando == 5:
        try:
            cursor.execute('''alter table pessoas
                           change column profissao prof varchar(20);''')
            print('''alter table pessoas
change column profissao prof varchar(20);''')

        except Exception as erro:
            print(f'Erro: {erro}')
    if comando == 6:
        try:
            cursor.execute('''alter table pessoas
                               drop column prof;''')
            print('''alter table pessoas
drop column prof;''')

        except Exception as erro:
            print(f'Erro: [{erro}')
    if comando == 7:
        try:
            cursor.execute('''alter table cursos
                           add column idcurso int first;''')
            print('''alter table cursos
add column idcurso int first;''')

        except Exception as erro:
            print(f'Erro: {erro}')
    if comando == 8:
        try:
            cursor.execute('''alter table cursos
                           add primary key(idcurso);''')
            print('''alter table cursos
add primary key(idcurso);''')

        except Exception as erro:
            print(f'Erro: {erro}')

    if comando == 9:
        try:
            cursor.execute('''alter table cursos
                                 drop column idcurso;''')
            print('''alter table pessoas
drop column idcurso;''')

        except Exception as erro:
            print(f'Erro: [{erro}')
    if comando == 10:
        try:
            cursor.execute('''alter table cursos
                           rename to curso;''')
            print('''alter table cursos
rename to curso;''')

        except Exception as erro:
            print(f'Erro: {erro}')
    if comando == 11:
        try:
            cursor.execute('''alter table curso
                           rename to cursos;''')
            print('''alter table curso
rename to cursos;''')

        except Exception as erro:
            print(f'Erro: {erro}')
    if comando == 12:
        try:
            cursor.execute('''alter table pessoas
                              add column ninja varchar(10);''')
            print('''alter table pessoas
add column profissao varchar(10);''')

        except Exception as erro:
            print(f'Erro: {erro}')
    if comando == 13:
        try:
            cursor.execute('''alter table pessoas
                              add foreign key (ninja)
                              references naruto(pessoa);''')
            print('''alter table pessoas
add foreign key (ninja)
references naruto(pessoa);''')
        except Exception as erro:
            print(f'Erro: {erro}')
    if comando == 14:
        try:
            cursor.execute('''update pessoas
                              set ninja = 'itachi'
                              where id = 1;''')
            print('''update pessoas
set ninja = itachi
where id = 1;''')
        except Exception as erro:
            print(f'Erro: {erro}')


