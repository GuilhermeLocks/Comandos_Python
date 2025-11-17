cpf = input('Digite o CPF: ')

numeros = ['0','1','2','3','4','5','6','7','8','9']
contador = 0

for c in cpf:
    contador += 1
    if c not in numeros:
        print('Erro: O CPF deve conter apenas números.')

if contador > 11:
    print('Erro: O CPF deve ter exatamente 11 dígitos e não mais que isso.')
elif contador < 11:
    print('Erro: O CPF deve ter exatamente 11 dígitos e não menos que isso.')
elif contador == 11:
    print('CPF válido.')
