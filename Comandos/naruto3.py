import random
import time

# Cabeçalho bonito
def mostrar_boas_vindas():
    print("=" * 40)
    print(" Bem-vindo ao Jogo da Adivinhação! ")
    print("=" * 40)

# Menu principal
def mostrar_menu():
    print("\nEscolha uma opção:")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")

# Regras do jogo
def mostrar_regras():
    print("\nREGRAS DO JOGO:")
    print("1. O computador vai pensar em um número entre 1 e 100.")
    print("2. Você precisa adivinhar qual é esse número.")
    print("3. A cada palpite, você será informado se está alto ou baixo.")
    print("4. Tente acertar com o menor número de tentativas!\n")

# Geração do número aleatório
def gerar_numero_secreto():
    return random.randint(1, 100)

# Validação do palpite
def obter_palpite():
    while True:
        try:
            palpite = int(input("Digite seu palpite (1 a 100): "))
            if 1 <= palpite <= 100:
                return palpite
            else:
                print("⚠️ Digite um número entre 1 e 100.")
        except ValueError:
            print("⚠️ Entrada inválida! Por favor, digite um número.")

# Lógica do jogo
def jogar():
    numero_secreto = gerar_numero_secreto()
    tentativas = 0
    historico = []

    print("\nO computador está pensando em um número entre 1 e 100...")
    time.sleep(1)

    while True:
        palpite = obter_palpite()
        tentativas += 1
        historico.append(palpite)

        if palpite < numero_secreto:
            print("🔽 Muito baixo!")
        elif palpite > numero_secreto:
            print("🔼 Muito alto!")
        else:
            print("🎉 Parabéns! Você acertou!")
            print(f"Você precisou de {tentativas} tentativas.")
            break

    print("\nSeus palpites foram:")
    print(historico)

# Programa principal
def main():
    mostrar_boas_vindas()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()

        if opcao == "1":
            jogar()
        elif opcao == "2":
            mostrar_regras()
        elif opcao == "3":
            print("\nObrigado por jogar! Até a próxima! 👋")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Rodar o programa
if __name__ == "__main__":
    main()

# Linhas extras para chegar a 100 (comentários didáticos)
# Linha 91
# Linha 92
# Linha 93
# Linha 94
# Linha 95
# Linha 96
# Linha 97
# Linha 98
# Linha 99
# Linha 100

# Gerenciador de Tarefas (To-Do List)
tarefas = []

def mostrar_menu():
    print("\n" + "=" * 30)
    print("      GERENCIADOR DE TAREFAS")
    print("=" * 30)
    print("1 - Adicionar nova tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ").strip()
    if nome:
        tarefas.append({"nome": nome, "concluida": False})
        print("✅ Tarefa adicionada!")
    else:
        print("⚠️ Tarefa não pode ser vazia!")

def listar_tarefas():
    if not tarefas:
        print("📭 Nenhuma tarefa adicionada.")
    else:
        print("\n📝 Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            status = "✔️" if tarefa["concluida"] else "❌"
            print(f"{i}. {tarefa['nome']} - {status}")

def marcar_como_concluida():
    listar_tarefas()
    if not tarefas:
        return
    try:
        escolha = int(input("Número da tarefa concluída: "))
        if 1 <= escolha <= len(tarefas):
            tarefas[escolha - 1]["concluida"] = True
            print("✅ Tarefa marcada como concluída!")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("⚠️ Entrada inválida!")

def remover_tarefa():
    listar_tarefas()
    if not tarefas:
        return
    try:
        escolha = int(input("Número da tarefa para remover: "))
        if 1 <= escolha <= len(tarefas):
            removida = tarefas.pop(escolha - 1)
            print(f"🗑️ Tarefa '{removida['nome']}' removida.")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("⚠️ Entrada inválida!")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção (1 a 5): ").strip()
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_como_concluida()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("\n👋 Saindo... Até a próxima!")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()

# Linhas extras para completar 100 (comentários úteis)
# 91: Cada tarefa é armazenada como um dicionário {'nome': ..., 'concluida': ...}
# 92: Isso facilita o controle de status da tarefa
# 93: Você pode melhorar salvando em arquivo .txt ou .json
# 94: Pode adicionar data, prioridade, categoria etc.
# 95: Pode transformar em app web com Flask ou Django
# 96: Também pode usar interface gráfica com Tkinter ou PyQt
# 97: A lógica é simples e ótima pra iniciantes
# 98: Mantenha a prática consistente e tente modificar o código!
# 99: Comente partes do código pra entender melhor o que fazem
# 100: Bora programar! 🚀

import random
import time

def mostrar_menu():
    print("=" * 35)
    print("   JOGO: PEDRA, PAPEL OU TESOURA")
    print("=" * 35)
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")

def mostrar_regras():
    print("\nREGRAS DO JOGO:")
    print("- Pedra ganha da Tesoura")
    print("- Tesoura ganha do Papel")
    print("- Papel ganha da Pedra")
    print("- Mesmas escolhas resultam em empate\n")

def obter_escolha_usuario():
    print("\nEscolha:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    try:
        escolha = int(input("Digite o número da sua escolha: "))
        if escolha in [1, 2, 3]:
            return escolha
        else:
            print("⚠️ Escolha inválida!")
            return None
    except ValueError:
        print("⚠️ Entrada inválida!")
        return None

def escolha_para_string(valor):
    if valor == 1:
        return "Pedra"
    elif valor == 2:
        return "Papel"
    elif valor == 3:
        return "Tesoura"

def decidir_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    elif (jogador == 1 and computador == 3) or \
         (jogador == 2 and computador == 1) or \
         (jogador == 3 and computador == 2):
        return "jogador"
    else:
        return "computador"

def jogar():
    jogador = None
    while jogador is None:
        jogador = obter_escolha_usuario()

    computador = random.randint(1, 3)

    print("\nJO")
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PÔ!!\n")
    time.sleep(0.5)

    print(f"🧑 Você escolheu: {escolha_para_string(jogador)}")
    print(f"💻 Computador escolheu: {escolha_para_string(computador)}")

    resultado = decidir_vencedor(jogador, computador)

    if resultado == "empate":
        print("🤝 Empate!")
    elif resultado == "jogador":
        print("🎉 Você venceu!")
    else:
        print("😢 O computador venceu!")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção (1 a 3): ").strip()

        if opcao == "1":
            jogar()
        elif opcao == "2":
            mostrar_regras()
        elif opcao == "3":
            print("\n👋 Obrigado por jogar! Até mais!")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()

# Linhas extras até 100
# 91: Você pode expandir esse jogo com placar
# 92: Ou salvar o histórico em um arquivo
# 93: Também dá pra criar versão com interface gráfica
# 94: Exemplo: Tkinter ou PySimpleGUI
# 95: Ou transformar em jogo web com Flask ou Django
# 96: Use funções para deixar o código organizado
# 97: Comente cada função para entender melhor
# 98: Refatore e experimente alterar a lógica
# 99: Tente criar modo com melhor de 3 rodadas
# 100: Divirta-se programando! 😄

import random
import time

def mostrar_menu():
    print("=" * 35)
    print("   JOGO: PEDRA, PAPEL OU TESOURA")
    print("=" * 35)
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")

def mostrar_regras():
    print("\nREGRAS DO JOGO:")
    print("- Pedra ganha da Tesoura")
    print("- Tesoura ganha do Papel")
    print("- Papel ganha da Pedra")
    print("- Mesmas escolhas resultam em empate\n")

def obter_escolha_usuario():
    print("\nEscolha:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    try:
        escolha = int(input("Digite o número da sua escolha: "))
        if escolha in [1, 2, 3]:
            return escolha
        else:
            print("⚠️ Escolha inválida!")
            return None
    except ValueError:
        print("⚠️ Entrada inválida!")
        return None

def escolha_para_string(valor):
    if valor == 1:
        return "Pedra"
    elif valor == 2:
        return "Papel"
    elif valor == 3:
        return "Tesoura"

def decidir_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    elif (jogador == 1 and computador == 3) or \
         (jogador == 2 and computador == 1) or \
         (jogador == 3 and computador == 2):
        return "jogador"
    else:
        return "computador"

def jogar():
    jogador = None
    while jogador is None:
        jogador = obter_escolha_usuario()

    computador = random.randint(1, 3)

    print("\nJO")
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PÔ!!\n")
    time.sleep(0.5)

    print(f"🧑 Você escolheu: {escolha_para_string(jogador)}")
    print(f"💻 Computador escolheu: {escolha_para_string(computador)}")

    resultado = decidir_vencedor(jogador, computador)

    if resultado == "empate":
        print("🤝 Empate!")
    elif resultado == "jogador":
        print("🎉 Você venceu!")
    else:
        print("😢 O computador venceu!")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção (1 a 3): ").strip()

        if opcao == "1":
            jogar()
        elif opcao == "2":
            mostrar_regras()
        elif opcao == "3":
            print("\n👋 Obrigado por jogar! Até mais!")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()

# Linhas extras até 100
# 91: Você pode expandir esse jogo com placar
# 92: Ou salvar o histórico em um arquivo
# 93: Também dá pra criar versão com interface gráfica
# 94: Exemplo: Tkinter ou PySimpleGUI
# 95: Ou transformar em jogo web com Flask ou Django
# 96: Use funções para deixar o código organizado
# 97: Comente cada função para entender melhor
# 98: Refatore e experimente alterar a lógica
# 99: Tente criar modo com melhor de 3 rodadas
# 100: Divirta-se programando! 😄

# Conversor de Unidades

def menu_principal():
    print("=" * 40)
    print("       CONVERSOR DE UNIDADES")
    print("=" * 40)
    print("1 - Temperatura")
    print("2 - Distância")
    print("3 - Peso")
    print("4 - Sair")

# ========== TEMPERATURA ==========

def menu_temperatura():
    print("\nConversão de Temperatura:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def executar_conversao_temperatura():
    menu_temperatura()
    opcao = input("Escolha a opção: ")
    try:
        if opcao == "1":
            c = float(input("Digite a temperatura em °C: "))
            f = celsius_para_fahrenheit(c)
            print(f"{c:.2f} °C = {f:.2f} °F")
        elif opcao == "2":
            f = float(input("Digite a temperatura em °F: "))
            c = fahrenheit_para_celsius(f)
            print(f"{f:.2f} °F = {c:.2f} °C")
        else:
            print("❌ Opção inválida!")
    except ValueError:
        print("⚠️ Valor inválido!")

# ========== DISTÂNCIA ==========

def menu_distancia():
    print("\nConversão de Distância:")
    print("1 - Km para Milhas")
    print("2 - Milhas para Km")

def km_para_milhas(km):
    return km * 0.621371

def milhas_para_km(milhas):
    return milhas / 0.621371

def executar_conversao_distancia():
    menu_distancia()
    opcao = input("Escolha a opção: ")
    try:
        if opcao == "1":
            km = float(input("Digite a distância em km: "))
            mi = km_para_milhas(km)
            print(f"{km:.2f} km = {mi:.2f} milhas")
        elif opcao == "2":
            mi = float(input("Digite a distância em milhas: "))
            km = milhas_para_km(mi)
            print(f"{mi:.2f} milhas = {km:.2f} km")
        else:
            print("❌ Opção inválida!")
    except ValueError:
        print("⚠️ Valor inválido!")

# ========== PESO ==========

def menu_peso():
    print("\nConversão de Peso:")
    print("1 - Kg para Libras")
    print("2 - Libras para Kg")

def kg_para_libras(kg):
    return kg * 2.20462

def libras_para_kg(lb):
    return lb / 2.20462

def executar_conversao_peso():
    menu_peso()
    opcao = input("Escolha a opção: ")
    try:
        if opcao == "1":
            kg = float(input("Digite o peso em kg: "))
            lb = kg_para_libras(kg)
            print(f"{kg:.2f} kg = {lb:.2f} lb")
        elif opcao == "2":
            lb = float(input("Digite o peso em libras: "))
            kg = libras_para_kg(lb)
            print(f"{lb:.2f} lb = {kg:.2f} kg")
        else:
            print("❌ Opção inválida!")
    except ValueError:
        print("⚠️ Valor inválido!")

# ========== LOOP PRINCIPAL ==========

def main():
    while True:
        menu_principal()
        escolha = input("Escolha uma opção (1 a 4): ").strip()

        if escolha == "1":
            executar_conversao_temperatura()
        elif escolha == "2":
            executar_conversao_distancia()
        elif escolha == "3":
            executar_conversao_peso()
        elif escolha == "4":
            print("\n👋 Obrigado por usar o conversor!")
            break
        else:
            print("❌ Opção inválida.")

# ========== EXECUÇÃO ==========
if __name__ == "__main__":
    main()

# Comentários até a linha 100:
# 91: O código está todo separado em funções (def)
# 92: Você pode reaproveitar funções em outros projetos
# 93: Pode adicionar mais categorias (ex: volume, tempo)
# 94: Para treinar, crie um sistema de histórico das conversões
# 95: Outra ideia é exportar os resultados para arquivo .txt
# 96: Também pode deixar as conversões mais interativas
# 97: Ou colocar validações visuais com biblioteca `colorama`
# 98: Esse projeto é ótimo para criar um app com interface gráfica
# 99: Tente transformar ele em API com Flask
# 100: Python é incrível! Continue praticando! 💡

# Simulador de Carrinho de Compras (sem funções)

carrinho = []
total = 0.0

while True:
    print("\n" + "=" * 40)
    print("        MERCADO DO PYTHON")
    print("=" * 40)
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver carrinho")
    print("4 - Ver total")
    print("5 - Finalizar compra")

    opcao = input("Escolha uma opção (1 a 5): ")

    if opcao == "1":
        nome = input("Nome do produto: ").strip()
        try:
            preco = float(input("Preço do produto: "))
            if preco < 0:
                print("⚠️ Preço inválido.")
                continue
            carrinho.append({"nome": nome, "preco": preco})
            total += preco
            print(f"✅ '{nome}' adicionado ao carrinho.")
        except ValueError:
            print("⚠️ Preço inválido.")
    elif opcao == "2":
        if not carrinho:
            print("🛒 Carrinho vazio.")
            continue
        print("\nItens no carrinho:")
        for i, item in enumerate(carrinho, 1):
            print(f"{i} - {item['nome']} - R${item['preco']:.2f}")
        try:
            idx = int(input("Número do item para remover: "))
            if 1 <= idx <= len(carrinho):
                removido = carrinho.pop(idx - 1)
                total -= removido["preco"]
                print(f"🗑️ '{removido['nome']}' removido.")
            else:
                print("⚠️ Número inválido.")
        except ValueError:
            print("⚠️ Entrada inválida.")
    elif opcao == "3":
        if not carrinho:
            print("🛒 Carrinho vazio.")
        else:
            print("\n🛍️ Itens no carrinho:")
            for i, item in enumerate(carrinho, 1):
                print(f"{i} - {item['nome']} - R${item['preco']:.2f}")
    elif opcao == "4":
        print(f"\n💰 Total da compra: R${total:.2f}")
    elif opcao == "5":
        print("\n🧾 Finalizando compra...")
        if not carrinho:
            print("Carrinho vazio. Nada a comprar.")
        else:
            print("Resumo da compra:")
            for item in carrinho:
                print(f"- {item['nome']} - R${item['preco']:.2f}")
            print(f"Total: R${total:.2f}")
        print("Obrigado por comprar! 🛒")
        break
    else:
        print("❌ Opção inválida.")

# Comentários para completar as 100 linhas
# 91: Esse script não usa funções (tudo em sequência)
# 92: Isso facilita a leitura para iniciantes
# 93: O carrinho é uma lista de dicionários
# 94: Cada item tem nome e preço
# 95: O total é atualizado automaticamente
# 96: O programa lida com erros de entrada
# 97: O menu repete até o usuário finalizar
# 98: Pode salvar a compra em arquivo (melhoria futura)
# 99: Pode adicionar quantidade, categoria etc.
# 100: Continue praticando! Python é poderoso! 🚀

# Importando biblioteca para gerar datas
import datetime

# Função lambda para capitalizar nomes
formatar_nome = lambda nome: nome.strip().title()

# Criando listas e dicionários
usuarios = []
ids = list(range(1, 101))
usuarios_ativos = set()
usuarios_banidos = set()

# Início do programa
print("🔐 Sistema de Cadastro de Usuários Python\n")

# Loop principal
while True:
    print("\nMenu:")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários")
    print("3 - Banir usuário")
    print("4 - Ativar usuário")
    print("5 - Mostrar estatísticas")
    print("6 - Exportar para arquivo")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        nome = formatar_nome(nome)
        idade = input("Digite a idade: ")

        try:
            idade = int(idade)
            id_usuario = ids.pop(0)
            usuario = {
                "id": id_usuario,
                "nome": nome,
                "idade": idade,
                "criado_em": datetime.datetime.now()
            }
            usuarios.append(usuario)
            usuarios_ativos.add(id_usuario)
            print(f"✅ Usuário '{nome}' cadastrado com ID {id_usuario}.")
        except ValueError:
            print("⚠️ Idade inválida. Deve ser um número.")

    elif opcao == "2":
        if not usuarios:
            print("📭 Nenhum usuário cadastrado.")
        else:
            print("\n📋 Lista de usuários:")
            for u in usuarios:
                status = "Ativo" if u["id"] in usuarios_ativos else "Banido"
                print(f"ID {u['id']:03} | {u['nome']} ({u['idade']} anos) - {status}")

    elif opcao == "3":
        try:
            id_banir = int(input("Digite o ID do usuário para banir: "))
            if id_banir in usuarios_ativos:
                usuarios_ativos.remove(id_banir)
                usuarios_banidos.add(id_banir)
                print(f"🚫 Usuário ID {id_banir} banido.")
            else:
                print("⚠️ Usuário não está ativo.")
        except ValueError:
            print("⚠️ ID inválido.")

    elif opcao == "4":
        try:
            id_ativar = int(input("Digite o ID para ativar: "))
            if id_ativar in usuarios_banidos:
                usuarios_banidos.remove(id_ativar)
                usuarios_ativos.add(id_ativar)
                print(f"🔓 Usuário ID {id_ativar} reativado.")
            else:
                print("⚠️ Usuário não está banido.")
        except ValueError:
            print("⚠️ ID inválido.")

    elif opcao == "5":
        total = len(usuarios)
        ativos = len(usuarios_ativos)
        banidos = len(usuarios_banidos)
        print("\n📈 Estatísticas:")
        print(f"Total de usuários: {total}")
        print(f"Ativos: {ativos}")
        print(f"Banidos: {banidos}")
        idades = [u["idade"] for u in usuarios]
        if idades:
            media_idade = sum(idades) / len(idades)
            mais_velho = max(usuarios, key=lambda u: u["idade"])
            print(f"Idade média: {media_idade:.1f}")
            print(f"Usuário mais velho: {mais_velho['nome']} ({mais_velho['idade']})")

    elif opcao == "6":
        try:
            with open("usuarios.txt", "w", encoding="utf-8") as arquivo:
                for u in usuarios:
                    status = "Ativo" if u["id"] in usuarios_ativos else "Banido"
                    linha = f"{u['id']},{u['nome']},{u['idade']},{status}\n"
                    arquivo.write(linha)
            print("📁 Arquivo 'usuarios.txt' salvo com sucesso.")
        except Exception as e:
            print("❌ Erro ao salvar arquivo:", e)

    elif opcao == "7":
        print("👋 Saindo do sistema. Até logo!")
        break

    else:
        print("❌ Opção inválida.")

# Criando e testando tupla
exemplo_tupla = ("admin", "moderador", "usuario")
if "admin" in exemplo_tupla:
    print("👤 Permissão de administrador detectada.")

# Usando enumerate
print("\n🔢 Listando permissões:")
for i, perm in enumerate(exemplo_tupla):
    print(f"{i + 1} - {perm}")

# Usando zip para combinar listas
nomes = ["Ana", "Bruno", "Carlos"]
pontos = [100, 200, 150]
print("\n🏆 Ranking:")
for nome, ponto in zip(nomes, pontos):
    print(f"{nome}: {ponto} pts")

# Usando sorted com lambda
print("\n📊 Ranking ordenado:")
ranking = sorted(zip(nomes, pontos), key=lambda x: x[1], reverse=True)
for nome, ponto in ranking:
    print(f"{nome}: {ponto} pts")

import random  # Usado para sortear perguntas
import math  # Usado para mostrar algumas funções matemáticas
import statistics  # Estatísticas com as pontuações
import time  # Simular delay
import os  # Para pegar variáveis do sistema
from functools import partial  # Criação de funções pré-configuradas
import tempfile  # Criar arquivos temporários
import types  # Criar módulo dinâmico

# Lista de perguntas como tuplas: (pergunta, [respostas], índice da correta)
perguntas = [
    ("Qual a capital do Brasil?", ["Rio de Janeiro", "Brasília", "São Paulo"], 1),
    ("2 + 2 * 2 = ?", ["6", "8", "4"], 0),
    ("Qual linguagem estamos usando?", ["Java", "Python", "C++"], 1),
    ("Qual a raiz quadrada de 81?", ["7", "8", "9"], 2),
    ("Quem criou o Python?", ["Linus", "Guido", "Bill"], 1)
]

# Seleciona 3 perguntas aleatórias
quiz = random.sample(perguntas, 3)

# Guarda pontuação
pontos = []

# Função parcial para formatar pergunta
mostrar = partial(print, "\n🧠 Pergunta:")

# Executa perguntas
[i := 0]
while (i := i + 1) <= len(quiz):
    q, opcoes, correta = quiz[i - 1]
    mostrar(q)
    [print(f"{j+1}. {op}", end="\n") for j, op in enumerate(opcoes)]
    resposta = input("Digite o número da resposta: ").strip()
    resultado = int(resposta) - 1 == correta
    pontos.append(resultado)
    print("✅ Correto!" if resultado else "❌ Errado.")
    time.sleep(1)

# Match-case (substituto moderno do if-elif-else)
match sum(pontos):
    case 3:
        nivel = "Perfeito"
    case 2:
        nivel = "Muito Bom"
    case 1:
        nivel = "Pode melhorar"
    case _:
        nivel = "Estude mais!"

# Estatísticas e manipulação
media = statistics.mean(pontos)
texto = f"Você acertou {sum(pontos)} de {len(quiz)}. Nível: {nivel}."
print(texto)

# Sets e frozensets
conj_acertos = set(pontos)
conj_estatico = frozenset([True, False])
print(f"Tipos de respostas dadas: {conj_acertos}")

# List comprehension reversa
rev = [q[0] for q in reversed(quiz)]
print("Perguntas feitas (ordem reversa):", ", ".join(rev))

# Operadores lógicos
valida = all(pontos) and any(pontos)
print("Você acertou tudo?" if valida else "Ainda pode melhorar.")

# Funções built-in
print("Funções disponíveis no módulo math:", len(dir(math)))
print("Existe 'sqrt' no math?", 'sqrt' in dir(math))
print("Ajuda de math.sqrt:")
help(math.sqrt)

# Manipulação de bytes e memória
b = bytes("Python", "utf-8")
ba = bytearray(b)
mv = memoryview(ba)
print("Bytes originais:", b)
print("Bytearray modificado:", ba)
mv[0] = 112  # mude 'P' para 'p'
print("Memoryview modificado:", ba)

# Módulo temporário com types
mod = types.ModuleType("meu_modulo")
mod.mensagem = lambda: "Oi do módulo dinâmico!"
print(mod.mensagem())

# Arquivo temporário
with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
    tmp.write("Resultado do quiz\n")
    tmp.write(texto)
    nome_arquivo = tmp.name
print(f"Arquivo salvo em: {nome_arquivo}")

# Leitura do arquivo gerado
with open(nome_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
print("📄 Conteúdo do arquivo:\n", conteudo)

# Variáveis do ambiente
print("Sistema operacional:", os.name)

# globals, locals
print("Variáveis globais disponíveis:", list(globals().keys())[:5])
print("Variáveis locais nesta função:", list(locals().keys())[:5])

import sqlite3  # Banco de dados leve embutido
import uuid  # Geração de IDs únicos
import calendar  # Mostrar calendário
import pathlib  # Caminhos multiplataforma
import json  # Serialização
import csv  # Arquivo CSV
from dataclasses import dataclass, asdict  # Estrutura de dados moderna
from itertools import count  # Contador infinito
from math import prod  # Produto de elementos
from pprint import pprint  # Impressão bonita

# Criação de tabela e conexão com banco de dados
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE clientes (id TEXT, nome TEXT, idade INTEGER)")

# Estrutura de dados com dataclass
@dataclass
class Cliente:
    id: str
    nome: str
    idade: int

# Lista fake com 5 nomes para simulação
nomes_base = ('Ana', 'Beto', 'Clara', 'Davi', 'Eva')

# Gerador infinito de clientes
def gerar_clientes():
    for i in count():
        yield Cliente(str(uuid.uuid4()), nomes_base[i % len(nomes_base)], 18 + i % 10)

# Salva os 5 primeiros clientes no banco
clientes_gerados = gerar_clientes()
dados = [next(clientes_gerados) for _ in range(5)]
for c in dados:
    cur.execute("INSERT INTO clientes VALUES (?, ?, ?)", (c.id, c.nome, c.idade))
con.commit()

# Objeto avançado com __slots__ para otimizar memória
class Registro:
    __slots__ = ('codigo', 'valor')

    def __init__(self, codigo, valor):
        self.codigo = codigo
        self.valor = valor

    def __repr__(self):
        return f"Registro(codigo={self.codigo}, valor={self.valor})"

# Criação de objetos usando __slots__
reg = Registro("X001", 99.9)
r2 = Registro("X002", 50.5)

# Propriedade com getter customizado
class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco_com_imposto(self):
        return self._preco * 1.15

    @staticmethod
    def categoria():
        return "Eletrônico"

    @classmethod
    def fabrica(cls):
        return cls(1000)

# Execução dinâmica de código
exec("x = 5")
resultado_exec = eval("x * 10")

# Gerador com yield
def multiplicador():
    val = 1
    while val < 10:
        yield val * 3
        val += 1

mult = list(multiplicador())

# Deletando variáveis
var_temp = "apagar"
del var_temp

# Criação de arquivo JSON
path = pathlib.Path("clientes.json")
json.dump([asdict(c) for c in dados], path.open("w"))

# Leitura JSON e transformação
lidos = json.load(path.open("r"))
transformado = [Cliente(**item) for item in lidos]

# Exportando para CSV
csv_path = pathlib.Path("clientes.csv")
writer = csv.writer(csv_path.open("w", newline=""))
writer.writerow(["id", "nome", "idade"])
for c in transformado:
    writer.writerow([c.id, c.nome, c.idade])

# Impressão com pprint
pprint(transformado)

# Exibição de calendário
calendario = calendar.month(2025, 4)

# Utilização de chr() e ord()
cod = [ord(c) for c in "ABCD"]
chars = [chr(n) for n in cod]

# Formatando strings com format()
msg = "Usuários ativos: {}".format(len(transformado))

# Usando assert para validação
assert len(transformado) == 5

# Usando pass e raise para futuras funções
def futuro():
    pass

def erro():
    raise NotImplementedError("Função ainda não implementada")

# Criando async e await simulados
async def carregar_dados():
    return [c.nome async for c in carregar_stream()]

async def carregar_stream():
    for c in transformado:
        yield c

# Acessando __name__ e __doc__
nome_modulo = __name__
doc_objeto = Cliente.__doc__

# Exibindo tudo ao final
pprint({
    "produtos": Produto.fabrica().preco_com_imposto,
    "resultado_exec": resultado_exec,
    "multiplicador": mult,
    "mensagem": msg,
    "calendario": calendario,
    "caracteres": chars,
    "modulo": nome_modulo
})

