print('\033[32m-='*17)
print('     SISTEMA DE AJUDA PyHELP')
print('-='*17)
def ajuda(a):
    print('\033[35m')
    help(a)
    print('\033[m')
ajuda(input('\033[m\033[34mFunção ou Biblioteca > \033[m'))