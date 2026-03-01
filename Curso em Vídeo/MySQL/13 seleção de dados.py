import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='', database='naruto')
cursor = con.cursor()

try:
    # tabela = input('Digite o nome da tabela: ')
    tabela = 'pessoa'

    cursor.execute(f'''SELECT * FROM {tabela}
                   order by nome;''')

    print(f'''SELECT * FROM {tabela}
order by nome;\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.execute(f'''SELECT nome, id, altura FROM {tabela}
                       order by nome desc;''')

    print(f'''\nSELECT nome, id, altura FROM {tabela}
order by nome desc;\n''')

    # 3. Buscar e imprimir dados
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.execute(f'''SELECT nome FROM {tabela}
                            where altura = '1.80'
                           order by nome desc;''')

    print(f'''\nSELECT nome FROM {tabela}
where altura = '1.80'
order by nome desc;\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)


    cursor.execute(f'''SELECT id, nome FROM {tabela}
                                where id between 1 and 6
                               order by id desc;''')

    print(f'''\nSELECT id, nome FROM {tabela}
where id between 1 and 6
order by id desc;\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)


    cursor.execute(f'''SELECT id, nome FROM {tabela}
                                    where id in (1, 2, 3)
                                   order by id desc;''')

    print(f'''\nSELECT id, nome FROM {tabela}
where id in (1, 2, 3)
order by id desc;\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)


    cursor.execute(f'''SELECT id, nome FROM {tabela}
                                        where id > 5 and id < 9
                                       order by id desc;''')

    print(f'''\nSELECT id, nome FROM {tabela}
where id > 5 and id < 9
order by id desc;\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT id, nome FROM {tabela}
                       where nome not like'%i%';''')

    print(f'''\nSELECT id, nome FROM {tabela}
where nome not like'%i%';\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT id, nome FROM {tabela}
                           where nome like '___u__';''')

    print(f'''\nSELECT id, nome FROM {tabela}
where nome like '___u__';\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT distinct nacionalidade FROM {tabela}
    order by nacionalidade;''')

    print(f'''\nSELECT distinct nacionalidade FROM {tabela}
order by nacionalidade;\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT count(*) FROM {tabela}
                        where nome = 'naruto';''')

    print(f'''\nSELECT count(*) FROM {tabela}
where nome = 'naruto';\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT max(altura) FROM {tabela};''')

    print(f'''\nSELECT max(altura) FROM {tabela};\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT min(altura) FROM {tabela};''')

    print(f'''\nSELECT min(altura) FROM {tabela};\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT sum(altura) FROM {tabela};''')

    print(f'''\nSELECT sum(altura) FROM {tabela};\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT avg(altura) FROM {tabela};''')

    print(f'''\nSELECT avg(altura) FROM {tabela};\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT * FROM {tabela}
                        where sexo = 'M';''')

    print(f'''\nSELECT * FROM {tabela}
where sexo = 'M';\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT * FROM {tabela}
                        where nacionalidade = 'Brazileiro';''')

    print(f'''\nSELECT * FROM {tabela}
where nacionalidade = 'Brazileiro';\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT * FROM {tabela}
                       where nome like 'n%' and nacionalidade = 'Japones' and sexo = 'M';''')

    print(f'''\nSELECT * FROM {tabela}
where nome like 'n%' and nacionalidade = 'Japones' and sexo = 'M';\n''')

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT nome FROM {tabela}
                           where nome like '%i%' and nacionalidade = 'Japones' and altura > '1.70';''')

    print(f'''\nSELECT nome FROM {tabela}
where nome like '%i%' and nacionalidade = 'Japones' and altura > '1.70';\n''')
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT max(altura) FROM {tabela}
                               where nacionalidade = 'Japones';''')

    print(f'''\nSELECT max(altura) FROM {tabela}
where nacionalidade = 'Japones';\n''')
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT avg(altura) FROM {tabela};''')
    print(f'''\nSELECT avg(altura) FROM {tabela};\n''')
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT count(altura) FROM {tabela}
                        where altura > 1.70;;''')
    print(f'''\nSELECT count(altura) FROM {tabela}
where altura > 1.70;\n''')
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT altura, count(altura) FROM {tabela}
                            group by altura;;''')
    print(f'''\nSELECT altura, count(altura) FROM {tabela}
group by altura;\n''')
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.execute(f'''SELECT altura, count(altura) FROM {tabela}
                                group by altura
                                having count(altura)>3;;''')
    print(f'''\nSELECT altura, count(altura) FROM {tabela}
group by altura
having count(altura)>3;\n''')
    result = cursor.fetchall()
    for row in result:
        print(row)
except Exception as erro:
    print(f'Erro: {erro}')
