import random
n1 = []
n1.append(input('Primeiro nome:'))
n1.append(input('Segundo nome:'))
n1.append(input('Terceiro nome:'))
n1.append(input('Quarto nome:'))
n2 = random.randint(0, 3)
print(n1[n2])