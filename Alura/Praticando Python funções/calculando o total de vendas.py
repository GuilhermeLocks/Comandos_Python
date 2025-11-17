def calculadora(text):
    num = 0
    for c in text.split():
        print(type(c), c)
        try:
            num += int(c)
        except:
            pass
    print(num)


calculadora(input(('Digite os valores das vendas:')))