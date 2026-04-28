
fim = 'False'
def ajuda(a):
    if a == 'fim':
        print('\033[31m-='*10)
        print('      ATE LOGO!')
        print('-='*10, '\033[m')
        return 'True'
    else:
        print('\033[35m')
        help(a)
        print('\033[m')
        return 'False'


while fim == 'False':
    print('\033[32m-='*17)
    print('     SISTEMA DE AJUDA PyHELP')
    print('-=' * 17)
    fim = ajuda(input('\033[m\033[34mFunção ou Biblioteca > \033[m'))