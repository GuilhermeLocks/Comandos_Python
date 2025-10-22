import random
um = 0
dois = 0
tres = 0
quatro = 0
cinco = 0
seis = 0
sete = 0
oito = 0
nove = 0
dez = 0
for c in range(1, 1000000):
    valor = random.randint(1, 10)
    print(c, valor)
    if valor == 1:
        um +=1
    if valor == 2:
        dois +=1
    if valor == 3:
        tres +=1
    if valor == 4:
        quatro +=1
    if valor == 5:
        cinco +=1
    if valor == 6:
        seis +=1
    if valor == 7:
        sete +=1
    if valor == 8:
        oito +=1
    if valor == 9:
        nove +=1
    if valor == 10:
        dez +=1

print(f'1  = {um}')
print(f'2  = {dois}')
print(f'3  = {tres}')
print(f'4  = {quatro}')
print(f'5  = {cinco}')
print(f'6  = {seis}')
print(f'7  = {sete}')
print(f'8  = {oito}')
print(f'9  = {nove}')
print(f'10 = {dez}')
