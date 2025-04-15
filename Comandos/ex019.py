import randomgjgshj
n1 = input('Primeiro nome:')
n2 = input('Segundo nome:')
n3 = input('Terceiro nome:')
n4 = input('Quarto nome:')

n5 = random.randint(1, 4)
if n5 == 1:
    print('O aluno escolhido foi', n1)
if n5 == 2:
    print('O aluno escolhido foi', n2)
if n5 == 3:
    print('O aluno escolhido foi', n3)
if n5 == n4:
    print('O aluno escolhido foi', n4)

list = [n1, n2, n3, n4]
n5 = random.choice(list)
print('O aluno escolhido foi', n5)
