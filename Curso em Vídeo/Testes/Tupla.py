lanche = ('hamburguer', 'batata frita', 'pudim', 'pizza')
print(lanche)
print(sorted(lanche))
print(sorted(lanche)[1])
print()
for c in sorted(lanche):
    if c =='hamburguer':
        c = 'comida'
    print(c)