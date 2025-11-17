tarefa = []
while True:
    while True:
        print('----------')
        opcao = input('''1. Adicionar tarefa 
2. Visualizar tarefas 
3. Remover tarefa 
4. Sair
Escolha uma opção: ''')
        print('----------')
        if opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4':
            break
        else:
            print('Opção invalida, tente novamente.')

    if opcao == '1':
        tarefa.append(input('Digite a tarefa: '))
        print('Tarefa adicionada!')

    if opcao == '2':
        cont = 0
        for c in tarefa:
            cont += 1
            print(f'{cont}. {c}')

    if opcao == '3':
        while True:
            try:
                removida = int(input('Digite o número da tarefa a ser removida: '))
                if removida > 0 and removida <= len(tarefa):
                    tarefa.remove(tarefa[removida-1])
                    break
            except:
                print('Erro: Nenhuma tarefa para remover.')

    if opcao == '4':
        break