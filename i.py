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

# Função para criar o HTML formatado com CSS
def gerar_html():
    # Carregar os dados dos arquivos JSON
    clientes = carregar_dados(arquivo_clientes)
    agendamentos = carregar_dados(arquivo_agendamentos)
    lucros = carregar_dados(arquivo_lucros)

    # Criar o conteúdo HTML
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
    
    # Adicionar clientes no HTML
    for cliente in clientes:
        html_content += f"""
            <tr>
                <td>{cliente['nome']}</td>
                <td>{cliente['idade']}</td>
                <td>{cliente['sexo']}</td>
            </tr>
        """
    
    # Continuar com agendamentos
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
    
    # Adicionar agendamentos no HTML
    for agendamento in agendamentos:
        html_content += f"""
            <tr>
                <td>{agendamento['nome']}</td>
                <td>{agendamento['horario']}</td>
                <td>{agendamento['servico']}</td>
                <td>R$ {agendamento['valor']:.2f}</td>
            </tr>
        """
    
    # Continuar com lucros
    html_content += """
            </table>
            <h2>Lucros do Dia</h2>
            <table>
                <tr>
                    <th>Dia</th>
                    <th>Lucro Total</th>
                </tr>
    """
    
    # Adicionar lucros no HTML
    for idx, lucro in enumerate(lucros, start=1):
        html_content += f"""
            <tr>
                <td>Dia {idx}</td>
                <td>R$ {lucro['lucro_dia']:.2f}</td>
            </tr>
        """
    
    # Finalizar o HTML
    html_content += """
            </table>
        </div>
    </body>
    </html>
    """
    
    # Salvar o conteúdo HTML em um arquivo
    with open("dados.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("Arquivo HTML gerado com sucesso: dados.html")

# Inicializando arquivos e executando a geração do HTML
inicializar_arquivos()
gerar_html()
