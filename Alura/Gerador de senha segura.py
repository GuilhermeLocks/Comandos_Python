from random import randint
minuscula = ['a', 'e', 'i', 'o', 'u']
maiuscula = ['A', 'E', 'I', 'O', 'U']
especial = ['@', '!', '#', '$', '%', '?', '*']
senha = []
for c in range(0, 4):
    senha.append(minuscula[randint(0, len(minuscula)-1)])
    senha.append(maiuscula[randint(0, len(maiuscula)-1)])
    senha.append(especial[randint(0, len(especial)-1)])
print('Senha gerada: ', end='')
for c in senha:
    print(c, end='')