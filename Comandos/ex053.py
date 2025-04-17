sms = str(input('Digite uma frase:'))
sms = sms.replace(' ', '').upper()
sms_2 = sms[::-1].upper()
if sms == sms[::-1]:
    print('A frase digitada e um palíndromo !')
else:
    print('Não é um palíndromo')