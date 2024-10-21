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

# Cliente 1
print("faça seu agendamento aqui abaixo:")
horário1 = input("selecione seu horário no horário de brasília: ")
nome1 = input("coloque seu nome: ")
valor1, servico1 = selecionar_servico()

# Exibindo os resultados
print("\nResumo do Agendamento:")
print("Cliente" , sep='/')
print(nome1, horário1,servico1, sep='/')

# Calculando e exibindo o valor total
total = valor1 
print(f"\nO valor total dos serviços é: R$ {total:.2f}")

