tarefa = []
while True:
    while True:
        opcao = input('''1. Adicionar tarefa 
2. Visualizar tarefas 
3. Remover tarefa 
4. Sair
Escolha uma opção: ''')
        if opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4':
            break
        else:
            print('Opção invalida, tente novamente.')

    if opcao == '1':
        tarefa.append(input('Digite a tarefa: '))
        print('Tarefa adicionada!')

    if opcao == '2':
        for c in tarefa:
            for v in range (1, tarefa.count(c) + 1):
                print(f'{v}. {c}')

    if opcao == '3':
        while True:
            try:
                removida = int(input('Digite o número da tarefa a ser removida: '))
                break
            except:
                print('erro')
        tarefa.remove(removida)

    if opcao == '4':
        break