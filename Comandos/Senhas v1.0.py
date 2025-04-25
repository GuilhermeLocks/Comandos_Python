import random
alg  = ('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789')
variavel = int(15)
codigo = []
codigo2 = ''
senha = str(input('Senha:'))
for c in range(0,len(senha)):
    if senha[c] in alg:
         codigo.append(int((alg.find(senha[c])+variavel)))
    else:
        codigo.append(variavel)
print(codigo)
#print(alg[0])
#print(len(alg))
#print(int(codigo.find('h'))+10)