menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":        
        valor = float(input("Insira o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R$ {valor:.2f}\n"
        
        else:
            print("Informe uma valor válido!")
    elif opcao == "2":
        valor = float(input("Insira o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente para saque!")
        
        elif excedeu_limite:
            print(f"Valor do saque excede o limite de: R$ {limite:.2f} por saque.")
        
        elif excedeu_saques:
            print("Quantidade de saques diários excedida!")
        
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Informe uma valor válido!")
    
    elif opcao == "3":
        print("\n============= Extrato ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f}")
        print("======================================")

    elif opcao == "0":
        break

else:
    print("Operação inválida, por favor selecione uma opção válida!")