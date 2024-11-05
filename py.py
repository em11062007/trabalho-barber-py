import json
import os

# Arquivos JSON para armazenar dados
arquivo_clientes = 'clientes.json'
arquivo_agendamentos = 'agendamentos.json'
arquivo_lucros = 'lucros.json'
arquivo_barbeiros = 'barbeiros.json'  # Arquivo para armazenar barbeiros

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

    if not os.path.exists(arquivo_barbeiros):
        with open(arquivo_barbeiros, 'w') as file:
            json.dump([], file)

# Função para salvar dados no arquivo JSON
def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as file:
        json.dump(dados, file, indent=4)

# Função para carregar dados do arquivo JSON
def carregar_dados(arquivo):
    with open(arquivo, 'r') as file:
        return json.load(file)

# Função para gerar o HTML formatado com CSS
def gerar_html():
    clientes = carregar_dados(arquivo_clientes)
    agendamentos = carregar_dados(arquivo_agendamentos)
    lucros = carregar_dados(arquivo_lucros)

    html_content = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dados da Barbearia</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }
            h1 {
                text-align: center;
                color: #333;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                background-color: white;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h2 {
                color: #444;
                border-bottom: 2px solid #f4f4f4;
                padding-bottom: 10px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }
            table, th, td {
                border: 1px solid #ddd;
            }
            th, td {
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #f8f8f8;
            }
        </style>
    </head>
    <body>
        <h1>Dados da Barbearia</h1>
        <div class="container">
            <h2>Clientes Cadastrados</h2>
            <table>
                <tr>
                    <th>Nome</th>
                    <th>Idade</th>
                    <th>Sexo</th>
                </tr>
    """
    
    for cliente in clientes:
        html_content += f"""
            <tr>
                <td>{cliente['nome']}</td>
                <td>{cliente['idade']}</td>
                <td>{cliente['sexo']}</td>
            </tr>
        """
    
    html_content += """
            </table>
            <h2>Agendamentos</h2>
            <table>
                <tr>
                    <th>Nome</th>
                    <th>Horário</th>
                    <th>Serviço</th>
                    <th>Valor</th>
                </tr>
    """
    
    for agendamento in agendamentos:
        html_content += f"""
            <tr>
                <td>{agendamento['nome']}</td>
                <td>{agendamento['horario']}</td>
                <td>{agendamento['servico']}</td>
                <td>R$ {agendamento['valor']:.2f}</td>
            </tr>
        """
    
    html_content += """
            </table>
            <h2>Lucros do Dia</h2>
            <table>
                <tr>
                    <th>Dia</th>
                    <th>Lucro Total</th>
                </tr>
    """
    
    for idx, lucro in enumerate(lucros, start=1):
        html_content += f"""
            <tr>
                <td>Dia {idx}</td>
                <td>R$ {lucro['lucro_dia']:.2f}</td>
            </tr>
        """
    
    html_content += """
            </table>
        </div>
    </body>
    </html>
    """
    
    with open("dados.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("Arquivo HTML gerado com sucesso: dados.html")

# Função para cadastrar cliente
def cadastrar_cliente():
    print("\nFaça seu cadastro aqui abaixo:")
    sexo = input("Insira seu sexo: ")
    idade = int(input("Coloque sua idade: "))
    nome = input("Coloque seu nome: ")
    senha = input("Crie uma senha: ")

    clientes = carregar_dados(arquivo_clientes)

    for cliente in clientes:
        if cliente['nome'] == nome:
            print(f"{nome} já está cadastrado!")
            return

    novo_cliente = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo,
        'senha': senha
    }
    clientes.append(novo_cliente)
    salvar_dados(arquivo_clientes, clientes)

    print("\nCadastro realizado com sucesso!")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Sexo: {sexo}")

# Função para cadastrar barbeiro
def cadastrar_barbeiro():
    print("\nFaça seu cadastro de barbeiro aqui abaixo:")
    nome = input("Coloque seu nome: ")
    idade = int(input("Coloque sua idade: "))
    sexo = input("Insira seu sexo: ")
    senha = input("Crie uma senha: ")

    barbeiros = carregar_dados(arquivo_barbeiros)

    for barbeiro in barbeiros:
        if barbeiro['nome'] == nome:
            print(f"{nome} já está cadastrado como barbeiro!")
            return

    novo_barbeiro = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo,
        'senha': senha
    }
    barbeiros.append(novo_barbeiro)
    salvar_dados(arquivo_barbeiros, barbeiros)

    print("\nCadastro de barbeiro realizado com sucesso!")

# Função para verificar a senha do barbeiro
def verificar_senha_barbeiro():
    nome = input("Insira seu nome: ")
    senha = input("Insira sua senha: ")

    barbeiros = carregar_dados(arquivo_barbeiros)

    for barbeiro in barbeiros:
        if barbeiro['nome'] == nome and barbeiro['senha'] == senha:
            return True
    print("Nome ou senha incorretos.")
    return False

# Função para calcular o lucro do dia
def calcular_lucro():
    if not verificar_senha_barbeiro():
        return

    print("\nFaça seu cálculo do dia logo abaixo:")
    lucro_total = 0
    opcoes_corte = {
        1: "Corte",
        2: "Barba",
        3: "Corte + Barba"
    }

    lucros = carregar_dados(arquivo_lucros)
    
    for i in range(1, 4):
        print(f"\nOpção {i}: {opcoes_corte[i]}")
        v1 = float(input(f"Coloque o valor do {opcoes_corte[i]}: R$ "))
        v2 = int(input(f"Coloque quantas pessoas realizaram o {opcoes_corte[i]}: "))
        lucro_total += v1 * v2

    lucro_dia = {'lucro_dia': lucro_total}
    lucros.append(lucro_dia)
    salvar_dados(arquivo_lucros, lucros)

    print("\nResumo do Lucro:")
    print(f"Lucro Total do Dia: R$ {lucro_total:.2f}")

# Função para agendar horário
def agendar_horario():
    print("\nFaça seu agendamento aqui abaixo:")
    horario = input("Selecione seu horário no horário de Brasília: ")
    nome = input("Coloque seu nome: ")
    
    agendamentos = carregar_dados(arquivo_agendamentos)

    for agendamento in agendamentos:
        if agendamento['nome'] == nome:
            print(f"{nome} já tem um horário agendado para {agendamento['horario']}!")
            return
    
    valor, servico = selecionar_servico()
    
    novo_agendamento = {
        'nome': nome,
        'horario': horario,
        'servico': servico,
        'valor': valor
    }
    agendamentos.append(novo_agendamento)
    salvar_dados(arquivo_agendamentos, agendamentos)

    print("\nResumo do Agendamento:")
    print(f"Cliente: {nome}")
    print(f"Horário: {horario}")
    print(f"Serviço: {servico}")
    print(f"Valor Total: R$ {valor:.2f}")

# Função para selecionar o serviço
def selecionar_servico():
    print("\nEscolha o serviço:")
    print("1 - Corte (R$ 30,00)")
    print("2 - Barba (R$ 20,00)")
    print("3 - Corte + Barba (R$ 45,00)")
    
    opcao = int(input("Selecione o número do serviço: "))
    
    if opcao == 1:
        return 30.00, "Corte"
    elif opcao == 2:
        return 20.00, "Barba"
    elif opcao == 3:
        return 45.00, "Corte + Barba"
    else:
        print("Opção inválida, selecione novamente.")
        return selecionar_servico()

# Função do menu principal
def menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Barbeiro")
        print("3 - Agendar Horário")
        print("4 - Calcular Lucro")
        print("5 - Gerar e Visualizar HTML")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            cadastrar_barbeiro()
        elif opcao == '3':
            agendar_horario()
        elif opcao == '4':
            calcular_lucro()
        elif opcao == '5':
            gerar_html()
        elif opcao == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicializando arquivos e chamando o menu principal
inicializar_arquivos()
menu()
