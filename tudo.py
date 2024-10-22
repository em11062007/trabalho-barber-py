 #Menu principal
def menu():
    print("Escolha uma das opções abaixo:")
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

# Execução do menu principal
menu()



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

# Função para calcular o lucro de cada corte
def soma(v1, v2):
    return v1 * v2

# Função para agendamento de horário
def agendar_horario():
    print("\nFaça seu agendamento aqui abaixo:")
    horario = input("Selecione seu horário no horário de Brasília: ")
    nome = input("Coloque seu nome: ")
    valor, servico = selecionar_servico()
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

# Exibindo o resumo do cadastro
    print("\nCadastro realizado com sucesso!")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Sexo: {sexo}")

# Função para calcular o lucro do dia
def calcular_lucro():
    print("\nFaça seu cálculo do dia logo abaixo:")
    lucro_total = 0
    opcoes_corte = {
        1: "cabelo",
        2: "Barba",
        3: "cabelo + Barba"
    }

#Loop para selecionar e calcular o lucro para cada tipo de corte
    for i in range(1, 4):
        print(f"\nOpção {i} - {opcoes_corte[i]}")
        v1 = int(input(f"Coloque o valor do {opcoes_corte[i]}: R$"))
        v2 = int(input(f"Coloque a quantidade de {opcoes_corte[i]} realizados: "))
        
        resultado = soma(v1, v2)
        print(f"O lucro para {opcoes_corte[i]} foi: R${resultado:.2f}")
        
# Somando o lucro de cada corte ao lucro total
        lucro_total += resultado

# Exibindo o lucro total no final
    print(f"\nO lucro total do dia foi: R${lucro_total:.2f}")

