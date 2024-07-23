saldo_global = 0.00
extrato_global = []
usuarios = []
contas = []
numero_conta = 1

def menu():
    menu_inicial = '''
-------------------------------------
          Menu Inicial         
-------------------------------------
 Digite a opção desejada:
                                       
 [1] - Realizar Operações                   
 [2] - Cadastrar Novo Usuário                        
 [3] - Criar Conta Corrente                      
 [4] - Sair                          
-------------------------------------
'''
    global usuarios
    global contas
    global numero_conta
    while True:
        option = input(menu_inicial)
        
        if option == "1":
            operacoes_bancarias()

        elif option == "2":
            novo_usuario = cadastro_usuario()
            if novo_usuario == False:
                pass
            else:
                usuarios.append(novo_usuario) 

        elif option == "3":
            nova_cc = cadastro_cc()
            if nova_cc == False:
                pass
            else:
                contas.append(nova_cc)
                numero_conta += 1

        elif option == "4":
            print("\nObrigado por usar o sistema bancário da DIO\n")
            break
        else:
            print("Opção inválida\nRepita a operação")   


def operacoes_bancarias():
    menu_operacoes = '''
-------------------------------------
          Menu de operações          
-------------------------------------
 Digite a opção de operação desejada:
                                       
 [1] - Depositar                     
 [2] - Sacar                         
 [3] - Extrato                       
 [4] - Sair                          
-------------------------------------
'''
    saques_realizados = 0
    global saldo_global
    global extrato_global
    limite_user = 3
    limite_saques_user = 3

    while True:
        option = input(menu_operacoes)
        
        if option == "1":
            retorno_deposito = deposito(saldo_global)

            if retorno_deposito[0] == False:
                saldo_global = retorno_deposito[1]
                extrato_global.append(retorno_deposito[2])

        elif option == "2":
            retorno_saque = saque(saldo= saldo_global, limite= limite_user, contagem_saques= saques_realizados, limite_saques= limite_saques_user)
            
            if retorno_saque[0] == False:
                saldo_global = retorno_saque[1]
                extrato_global.append(retorno_saque[2])
                saques_realizados = retorno_saque[3]


        elif option == "3":
            extrato(saldo_global, extrato= extrato_global)

        elif option == "4":
            print("\nSaindo do Sistema de Operações...\n")
            break
        else:
            print("Opção inválida\nRepita a operação")

def cadastro_usuario():
    global usuarios
    print("\n| CPF do Usuário |")
    while True:
        cpf = input("Digite o CPF que deseja cadastrar:")

        if len(cpf) == 11 and cpf.isdigit():
            break
        else: 
            print("CPF inválido! digite um CPF com 11 números.")      

    cpf_exist = False

    for user in usuarios:
        if user["cpf"] == cpf:
            cpf_exist = True
            break


    if cpf_exist == False:
        
        print("\n| Nome do Usuário |")
        nome = input("Digite o nome do usuário:")
        
        print("\n| Endereço do Usuário |")
        rua = input("Digite o nome da Rua:")
        numero = input("Digite o numero da moradia:")
        bairro = input("Digite o bairro:")
        cidade = input("Digite a cidade:")
        estado = input("Digite a sigla do estado:")

        adress = f"{rua}, {numero} - {bairro} - {cidade}/{estado}"

        print("\n| Data de Nascimento do Usuário |")
        while True:
            dia = int(input("Digite o dia:"))
            if  0 < dia <= 31: 
                break
            else:
                print("Dia inválido! Digite novamente.")
        while True:
            mes = int(input("Digite o mes:"))
            if  0 < mes <= 12: 
                break
            else:
                print("Mes inválido! Digite novamente.")
        while True:
            ano = int(input("Digite o ano:"))
            if  1900 < ano <= 2024: 
                break
            else:
                print("Dia inválido! Digite novamente.")

        data = f"{dia}/{mes}/{ano}"

        new_user = {"cpf": cpf, "nome": nome, "endereco": adress, "data": data}
        return new_user
    else:
        print ("\nUsuário já cadastrado no Sistema!")
        return False
    
def cadastro_cc():
    while True:
        cpf_conta = input("Digite o cpf do usuário que deseja cadastrar a conta:")

        if len(cpf_conta) == 11 and cpf_conta.isdigit:
            break        
        else:
            print("CPF inválido! digite um CPF com 11 números.")

    cpf_exist = False
    for user in usuarios:
        
        if user["cpf"] == cpf_conta:
                cpf_exist = True

    if cpf_exist == True:
        agencia = "0001"
        global numero_conta
        print(f"Novo usuario de CPF:{cpf_conta}, cadastrado na agência:{agencia} e conta de numero:{numero_conta}")
        new_account = {"cpf": cpf_conta, "agencia": agencia, "conta": numero_conta}       
        return new_account



    else:
        print("\nCPF sem cadastro, cadastre o usuário antes de criar uma conta corrente!")
       
        return False




def deposito(saldo: float, /):

    print("Opção de Depósito selecionada:")
    valor = float(input("Digite o valor a ser depositado:"))
    operation_fail = True
    extrato = ""
    if valor > 0.00:
        saldo += valor
        extrato = (f"\n- Depósito realizado\nValor depositado: R${valor:.2f}")
        print(f"Depósito no valor de R${valor:.2f} realizado!")
        
        operation_fail = False

    else:
        print("\nValor de depósito inválido\nRepita a operação")

    return  [operation_fail, saldo, extrato]

def saque(*, saldo: float, limite:float, contagem_saques: int, limite_saques: int):

    print("Opção de saque selecionada:")
    operation_fail = True
    extrato = ""
    if contagem_saques < limite_saques:
        valor = float(input("Digite o valor a ser sacado (limite de R$500,00 por saque):"))

        if saldo >= valor:
            if valor > 0.00 and valor <= 500.00:
                saldo -= valor
                extrato = (f"\n- Saque realizado\nValor sacado: R${valor:.2f}")
                contagem_saques += 1
                print(f"Saque no valor de R${valor:.2f} realizado!")

                operation_fail = False

            else:
                print("\nValor de saque inválido\nRepita a operação") 

        else:
            print("\nSaldo insuficiente\nRepita a operação")
    else:
        print("\nLimite de operações de saque diário atingido")

    return [operation_fail, saldo, extrato, contagem_saques]

def extrato(saldo: float, /, *, extrato: list):
    
    print("\n---------------Extrato---------------")

    if extrato:
        for action in extrato:
            print(action)
    else:
        print("- Nenhuma movimentação realizada.")
    
    print(f"\nSaldo disponível: R$ {saldo:.2f}")
    print("--------------------------------------")

menu()