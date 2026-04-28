peso = float(input('Qual seu peso? (Kg)'))
altura = float(input('Qual sua altura? (M)'))
imc = peso/ (altura*altura)
imc = float('{:.1f}'.format(imc))
if imc < 18.5:
    print('baixo peso')
elif 24.9 >= imc >= 18.5:
    print('peso normal')
elif 29.9 >= imc >= 25:
    print('excesso de peso')
elif 35 >= imc >= 30:
    print('obesidade')
else:
    print('obesidade extrema')


