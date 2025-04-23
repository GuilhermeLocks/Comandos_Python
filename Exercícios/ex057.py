while True:
    sexo = input('Informe seu sexo :[M/F]').isupper()
    if sexo == 'M' or sexo == 'F':
        print(sexo)
        break
    else:
        print('Tente novamente')