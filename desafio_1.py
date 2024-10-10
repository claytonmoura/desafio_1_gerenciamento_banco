def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não existe, crie um usuário primeiro!")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com o CPF informado!")
        return

    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe a data de nascimento [dd-mm-aaaa]: ")
    endereco = input("Informe o endereço [logradouro, Nº - bairro - cidade/sigla estado]: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def exibir_extrato(saldo, /, *, extrato):
    print("\n============= Extrato ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: {saldo:.2f}")
    print("======================================")

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

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
    
    return saldo, extrato, limite, numero_saques, limite_saques

def depositar(saldo, valor, extrato, /):    
    if valor > 0:
                saldo += valor
                extrato += f"\nDepósito: R$ {valor:.2f}\n"
    else:
                print("Informe uma valor válido!")
    
    return saldo, extrato

def menu():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuario
    [5] Criar conta
    [0] Sair

    => """
    return input(menu)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Insira o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)        
            
        elif opcao == "2":
            valor = float(input("Insira o valor do saque: "))
            saldo, extrato, limite, numero_saques, LIMITE_SAQUES = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)            
        
        elif opcao == "3":
             exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)            

        elif opcao == "0":
            break

    else:
        print("Operação inválida, por favor selecione uma opção válida!")

main()