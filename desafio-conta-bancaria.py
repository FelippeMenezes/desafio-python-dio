saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_usuarios = []
AGENCIA = "0001"
contas = []

def menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES): 
    print("""
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[c] Criar conta
[l] Listar contas
[q] Sair""")
    print("=> ", end="")
    opcao = input()
    if opcao == "d":
        print("\nInforme o valor do depósito: ", end="")
        valor = input()
        saldo, extrato = depositar(saldo, extrato, valor)
    elif opcao == "s":
        print("\nInforme o valor do saque: ", end="")
        valor = input()
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
    elif opcao == "e":
        mostra_extrato(saldo, extrato=extrato)
    elif opcao == "u":
        criar_usuario(lista_usuarios)
    elif opcao == "c":
        criar_conta(contas, lista_usuarios)
    elif opcao == "q":
        exit()
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)

def depositar(saldo, extrato, valor, /):
    if valor.isdigit() == False:
        print("\nOperação falhou! O valor informado é inválido.")
        menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)
    else:
        valor = float(valor)
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)
    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor.isdigit() == False:
        print("\nOperação falhou! O valor informado é inválido.")
        menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)
    elif float(valor) > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)
    elif float(valor) > limite:
        print("Operação falhou! O valor do saque excede o limite.")
        menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
        menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)
    else:
        valor = float(valor)
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)
    return saldo, extrato, numero_saques

def mostra_extrato(saldo, /, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==========================================")
        menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)

def criar_usuario(lista_usuarios):
    print("Informe o CPF(Somente números): ", end="")
    cpf = input()
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            print(f"CPF já cadastrado com o nome {usuario['nome']}.")
            menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)
            return
    print("Informe o nome completo: ", end="")
    nome = input()
    print("Informe a data de nascimento (dd-mm-aaaa): ", end="")
    data_nascimento = input()
    print("Informe o endereço(logradouro, nro - bairro - cidade/sigla estado): ", end="")
    endereco = input()
    usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    lista_usuarios.append(usuario)
    print("Usuário criado com sucesso!")
    menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)

def criar_conta(contas, lista_usuarios):
    print("Informe o CPF do usuário: ", end="")
    cpf = input()
    numero_conta = f"{AGENCIA}{len(contas) + 1}"
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
            contas.append(conta)
            print("Conta criada com sucesso!")
            menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)
            return contas
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")
    menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)

menu(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)

# [d] Depositar
# [s] Sacar
# [e] Extrato
# [q] Sair

# => """

# saldo = 0
# limite = 500
# extrato = ""
# numero_saques = 0
# LIMITE_SAQUES = 3

# while True:

#     opcao = input(menu)

#     if opcao == "d":
#         valor = float(input("Informe o valor do depósito: "))

#         if valor > 0:
#             saldo += valor
#             extrato += f"Depósito: R$ {valor:.2f}\n"

#         else:
#             print("Operação falhou! O valor informado é inválido.")

#     elif opcao == "s":
#         valor = float(input("Informe o valor do saque: "))

#         excedeu_saldo = valor > saldo

#         excedeu_limite = valor > limite

#         excedeu_saques = numero_saques >= LIMITE_SAQUES

#         if excedeu_saldo:
#             print("Operação falhou! Você não tem saldo suficiente.")

#         elif excedeu_limite:
#             print("Operação falhou! O valor do saque excede o limite.")

#         elif excedeu_saques:
#             print("Operação falhou! Número máximo de saques excedido.")

#         elif valor > 0:
#             saldo -= valor
#             extrato += f"Saque: R$ {valor:.2f}\n"
#             numero_saques += 1

#         else:
#             print("Operação falhou! O valor informado é inválido.")

#     elif opcao == "e":
#         print("\n================ EXTRATO ================")
#         print("Não foram realizadas movimentações." if not extrato else extrato)
#         print(f"\nSaldo: R$ {saldo:.2f}")
#         print("==========================================")

#     elif opcao == "q":
#         break

#     else:
#         print("Operação inválida, por favor selecione novamente a operação desejada.")
