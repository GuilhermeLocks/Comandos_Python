c = 0
while c < 3 :
    c += 1
    print(c)
print('')
while True:
    f = input('Digite um valor: ')
    if f.isnumeric() == True:
        print(int(f)*6)
        break
    else:
        print('Tente novamente.')


