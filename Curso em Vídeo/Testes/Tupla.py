lanche = ('hamburguer', 'batata frita', 'pudim', 'pizza')
lanche_lista = []
print(lanche)
print(sorted(lanche))
print(sorted(lanche)[1])
print()
for c in sorted(lanche):
    if c =='hamburguer':
        c = 'comida'
    print(c)
print()
for c in lanche:
    print(c)
    lanche_lista.append(c)
print()
for c in lanche_lista:
    print(c)