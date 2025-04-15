print('Manipular cadeias de texto')

n1 = str('0123456789')

print('Fatiamento')
print(n1)
print(n1[0])
print(n1[0:10])
print(n1[0:10:2])
print(n1[:10:2])
print(n1[0::2])
print(n1[::2])

print('Análise')
print(len(n1))
print(n1.count('9'))
print(n1.count(n1, 0, 5))
print(n1.find('1'))
print(n1.find('58'))
print('56' in n1)
n1 = n1.replace('56', '55')
print(n1)

n1 = ' python pyton '

print(n1.upper())
print(n1.lower())

print(n1.capitalize())
print(n1.title())

print(n1.strip())
print(n1.lstrip())
print(n1.rstrip())
print(n1.split())
print(('-'.join(n1)))
print('''zsf
sdf
sdf
sdf''')
print(n1.split()[1][0])