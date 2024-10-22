import json
import os

# Arquivos JSON para armazenar dados
arquivo_clientes = 'clientes.json'
arquivo_agendamentos = 'agendamentos.json'
arquivo_lucros = 'lucros.json'

# Verificando se os arquivos existem, senão cria vazios
def inicializar_arquivos():
    if not os.path.exists(arquivo_clientes):
        with open(arquivo_clientes, 'w') as file:
            json.dump([], file)  # Inicializa com uma lista vazia
    
    if not os.path.exists(arquivo_agendamentos):
        with open(arquivo_agendamentos, 'w') as file:
            json.dump([], file)
    
    if not os.path.exists(arquivo_lucros):
        with open(arquivo_lucros, 'w') as file:
            json.dump([], file)

# Função para salvar dados no arquivo JSON
def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as file:
        json.dump(dados, file, indent=4)

# Função para carregar dados do arquivo JSON
def carregar_dados(arquivo):
    with open(arquivo, 'r') as file:
        return json.load(file)

# Definindo os preços dos serviços
preco_corte = 30.00
preco_barba = 20.00
preco_corte_e_barba = 45.00

# Função para selecionar o serviço e retornar o valor e a descrição do serviço
def selecionar_servico():
    print("\nEscolha o serviço:")
    print("1 - Corte (R$ 30,00)")
    print("2 - Barba (R$ 20,00)")
    print("3 - Corte + Barba (R$ 45,00)")
    
    opcao = int(input("Selecione o número do serviço: "))
    
    if opcao == 1:
        return preco_corte, "Corte"
    elif opcao == 2:
        return preco_barba, "Barba"
    elif opcao == 3:
        return preco_corte_e_barba, "Corte + Barba"
    else:
        print("Opção inválida, selecione novamente.")
        return selecionar_servico()

# Função para agendamento de horário
def agendar_horario():
    print("\nFaça seu agendamento aqui abaixo:")
    horario = input("Selecione seu horário no horário de Brasília: ")
    nome = input("Coloque seu nome: ")
    
    # Carregando agendamentos existentes
    agendamentos = carregar_dados(arquivo_agendamentos)

    # Verifica se o usuário já tem horário agendado
    for agendamento in agendamentos:
        if agendamento['nome'] == nome:
            print(f"{nome} já tem um horário agendado para {agendamento['horario']}!")
            return
    
    valor, servico = selecionar_servico()
    
    # Adicionando novo agendamento
    novo_agendamento = {
        'nome': nome,
        'horario': horario,
        'servico': servico,
        'valor': valor
    }
    agendamentos.append(novo_agendamento)
    salvar_dados(arquivo_agendamentos, agendamentos)

    # Exibindo o resumo do agendamento
    print("\nResumo do Agendamento:")
    print(f"Cliente: {nome}")
    print(f"Horário: {horario}")
    print(f"Serviço: {servico}")
    print(f"Valor Total: R$ {valor:.2f}")

# Função para cadastro de cliente
def cadastrar_cliente():
    print("\nFaça seu cadastro aqui abaixo:")
    sexo = input("Insira seu sexo: ")
    idade = int(input("Coloque sua idade: "))
    nome = input("Coloque seu nome: ")

    # Carregando clientes existentes
    clientes = carregar_dados(arquivo_clientes)

    # Verifica se o cliente já está cadastrado
    for cliente in clientes:
        if cliente['nome'] == nome:
            print(f"{nome} já está cadastrado!")
            return

    # Adicionando novo cliente
    novo_cliente = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo
    }
    clientes.append(novo_cliente)
    salvar_dados(arquivo_clientes, clientes)

    # Exibindo o resumo do cadastro
    print("\nCadastro realizado com sucesso!")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Sexo: {sexo}")

# Função para calcular o lucro de cada serviço
def soma(v1, v2):
    return v1 * v2

# Função para calcular o lucro do dia
def calcular_lucro():
    print("\nFaça seu cálculo do dia logo abaixo:")
    lucro_total = 0
    opcoes_corte = {
        1: "Corte",
        2: "Barba",
        3: "Corte + Barba"
    }

    # Carregando lucros anteriores
    lucros = carregar_dados(arquivo_lucros)
    
    # Loop para selecionar e calcular o lucro para cada tipo de corte
    for i in range(1, 4):
        print(f"\nOpção {i} - {opcoes_corte[i]}")
        v1 = int(input(f"Coloque o valor do {opcoes_corte[i]}: R$"))
        v2 = int(input(f"Coloque a quantidade de {opcoes_corte[i]} realizados: "))
        
        resultado = soma(v1, v2)
        print(f"O lucro para {opcoes_corte[i]} foi: R${resultado:.2f}")
        
        # Somando o lucro de cada corte ao lucro total
        lucro_total += resultado

    # Salvando o lucro do dia
    lucros.append({'lucro_dia': lucro_total})
    salvar_dados(arquivo_lucros, lucros)

    # Exibindo o lucro total no final
    print(f"\nO lucro total do dia foi: R${lucro_total:.2f}")

# Menu principal
def menu():
    print("\nEscolha uma das opções abaixo:")
    print("1 - Agendar horário")
    print("2 - Cadastrar cliente")
    print("3 - Calcular lucro do dia")
    
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        agendar_horario()
    elif opcao == 2:
        cadastrar_cliente()
    elif opcao == 3:
        calcular_lucro()
    else:
        print("Opção inválida. Tente novamente.")
        menu()

# Inicializando os arquivos JSON
inicializar_arquivos()

# Execução do menu principal
menu()
