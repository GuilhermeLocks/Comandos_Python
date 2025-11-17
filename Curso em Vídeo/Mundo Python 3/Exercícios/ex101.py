import datetime
def voto(a):
    idade = datetime.date.today().year - a
    print('Com {} anos: '.format(idade), end=' ')
    if idade < 16:
        return 'NÃO VOTA'
    elif 18 > idade >= 16:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'

estado = voto(int(input('Em qual ano você nasceu ? ')))
print(estado)