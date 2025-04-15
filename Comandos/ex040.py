while True:

    primeira_nota = float(input('Primeira nota:'))
    segunda_nota = float(input('Segunda nota:'))
    media = (primeira_nota+segunda_nota)/2

    if media <= float(10) and media >= float(7):
        print('Aprovado')
        break
    elif media < 7 and media > 3:
        break
        print('Recuperacao')
    elif media <3 and media >=0:
        print('Reprovado')
        break
    else:
        print('Notas invalidas')