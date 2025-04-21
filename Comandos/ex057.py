while True:
    sexo = input('Informe seu sexo :[M/F]').upper()
    if sexo == 'M' or sexo == 'F':
        print(sexo)
        break
    else:
        print('Tente novamente')