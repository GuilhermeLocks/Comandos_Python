numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte',
while True:
    valor = input('Digite uma valor entre 0 e 20: ')
    if valor.isnumeric() == True:
        valor = int(valor)
        if valor >= 0 and valor <= 20:
            print(numeros[valor])
        else:
            print('Valor informado invalido tente novamente.')
    else:
        print('Comando invalido, tente novamente.')
