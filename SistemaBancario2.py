saldo_global = 0.00
extrato_global = []


def Menu():
    mensagem_menu = '''
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
        option = input(mensagem_menu)
        
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
            print("\nObrigado por usar o sistema bancário da DIO\n")
            break
        else:
            print("Opção inválida\nRepita a operação")

def deposito(saldo: float):

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

def extrato(saldo: float, *, extrato: list):
    
    print("\n---------------Extrato---------------")

    if extrato:
        for action in extrato:
            print(action)
    else:
        print("- Nenhuma movimentação realizada.")
    
    print(f"\nSaldo disponível: R$ {saldo:.2f}")
    print("--------------------------------------")

Menu()

