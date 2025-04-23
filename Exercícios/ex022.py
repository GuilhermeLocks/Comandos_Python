n1 = []
n2 = 0
n1 = str(input('Digige seu nome completo:'))

print(n1.upper())

print(n1.lower())

for c in range(0, len(n1.split())):
    n2 += len(n1.split()[c])
print(n2)

print(len(n1.split()[0]))

#guilherme da silva locks