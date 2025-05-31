def situacao(* num, sit=False):
    maior = menor = total = cont = media = 0
    dicionario = {'maior':0, 'menor':0}
    for c in num:
        total += c
        cont += 1
        if dicionario['maior'] == 0:
            dicionario['maior'] = c
        if dicionario['maior'] < c:
            dicionario['maior'] = c
        if dicionario['menor'] == 0:
            dicionario['menor'] = c
        if dicionario['menor'] > c:
            dicionario['menor'] = c
    dicionario['total'] = cont
    dicionario['media'] = total/cont
    print(dicionario)




situacao(10, 10, 10, sit=True)