lista_total = []
lista_temporaria = []
continuar = ''
aluno = 0
while continuar != 'N':
    lista_temporaria.append(str(input('Nome: ')))
    lista_temporaria.append(float(input('Nota 1: ')))
    lista_temporaria.append(float(input('Nota 2: ')))
    lista_total.append(lista_temporaria[:])
    lista_temporaria.clear()
    while True:
        continuar = input('Quer continuar? [S/N]').upper()
        if continuar.isalpha() == True:
            continuar =  str(continuar)
            break
        elif continuar != 'N' or continuar != 'S':
            print('Comando invalido, tente novamente.')
        else:
            print('Comando invalido, tente novamente.')
print('-='*30)
print('No. NOME     MÉDIA')
print('-'*20)
for c in range(0, len(lista_total)):
    print('{}   {}        {}'.format(c,     lista_total[c][0], (lista_total[c][1] + lista_total[c][2])))
print('-'*20)
print('-='*30)
while aluno != 999:
    while True:
        aluno = input('Mostrar notas de qual aluno? (999 interrompe)')
        if aluno.isnumeric() == True:
            aluno = int(aluno)
        for c in range(0, len(lista_total)):
            if aluno == c:
                break
        if aluno == 999:
            break
        print('Notas de {} são {} e {}'.format(lista_total[aluno][0], lista_total[aluno][1], lista_total[aluno][2]))