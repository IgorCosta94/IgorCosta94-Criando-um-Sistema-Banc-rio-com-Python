menu = """
=============================
|| Operações:              ||
|| [d] Deposito            ||
|| [s] Saque               ||
|| [e] Extrato             ||
|| [x] Sair                ||
=============================
===>"""

extrato = ""
saldo = 0
saques_diarios = 3
valor_maximo_de_saque = 500.00

#Mensagens de erro usadas nas operações de saque e depósito
operacao_invalida ="\nOperação informada inválida, por favor selecione novamente a operação." 
deposito_invalido ="\nErro, valor informado não é válido. Informe um valor válido."
saldo_insuficiente = "\nNão foi possível realizar o saque. Saldo insuficiente."
saque_excedeu_limite = "\nNão foi possível realizar o saque. O valor do saque excedeu o limite."
saque_invalido = "\nNão foi possível realizar o saque. O valor informado é inválido."
limite_de_saques_alcancado = "\nNão foi possível realizar o saque. Número máximo de saques do dia alcançado."

operacao = input(menu)
while operacao != "x":

    if operacao == "d":
        valor_do_deposito = float(input("Informe o valor do depósito: "))
    
        if valor_do_deposito > 0:
            saldo += valor_do_deposito
            extrato += f"Depósito: R$ {valor_do_deposito:.2f}\n"
        else:
            print(deposito_invalido)
    
    elif operacao == "s":
        valor_do_saque = float(input("Informe o valor do saque: "))

        if valor_do_saque > saldo:
            print(saldo_insuficiente)

        elif valor_do_saque > valor_maximo_de_saque:
            print(saque_excedeu_limite)
        
        elif saques_diarios == 0:
            print(limite_de_saques_alcancado)
        
        elif valor_do_saque > 0:
            saldo -= valor_do_saque
            extrato += f"Saque: R$ {valor_do_saque: .2f}\n"
            saques_diarios -= 1
        
        else:
            print(saque_invalido)

    elif operacao == "e":
        print("\n=========================================\n"
            "================ EXTRATO ================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================\n" \
        "=========================================")

    else:
        print(operacao_invalida)

    operacao = input(menu)
