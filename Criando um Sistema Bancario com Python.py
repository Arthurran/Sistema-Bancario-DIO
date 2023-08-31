
menu = '''
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

valor = 0.00
saldo = 0.00
extrato = []
saldo_count = 0

while True:
    option = (input(menu))
    
    if option == "1":
        print("Opção de Desposito selecionada:")
        valor = float(input("Digite o valor a ser depositado:"))

        if valor > 0.00:
            saldo += valor
            extrato.append (f"\nDeposito realizado\nValor depositado: R$ {valor:.2f}")

        else:
            print("\nValor de despósito inválido\nRepita a operação") 

    elif option == "2":
        print("Opção de saque selecionada:")

        if saldo_count < 3:
            valor = float(input("Digite o valor a ser sacado (limite de R$500,00 por saque):"))

            if saldo >= valor:
                if valor > 0.00 and valor <= 500.00:
                    saldo -= valor
                    extrato.append (f"\nSaque realizado\nValor sacado: R$ {valor:.2f}")
                    saldo_count += 1

                else:
                    print("\nValor de saque inválido\nRepita a operação") 

            else:
                print("\nSaldo insuficiente\nRepita a operação")

        else:
            print("\nLimite de operações de saque diário atingido")

    elif option == "3":
        print("\n---------------Extrato---------------")

        for action in extrato:
            print(action)
        
        print(f"\n\nSaldo disponivel: R$ {saldo:.2f}")
        print("\n--------------------------------------")

    elif option == "4":
        print("\nObrigado por usar o sistema bancário da DIO\n1")
        break

    else:
        print("Opção inválida\nRepita a operação")