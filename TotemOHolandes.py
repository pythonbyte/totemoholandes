import os
def clear():
    clear = os.system('cls')
    return clear

contador = 1
while True:
    while True:
        nome = ""
        alteracao = ""
        bebida = ""
        valorprato = float
        print("--------------------------------")
        print(" SEJA BEM VINDO AO RESTAURANTE ")
        print("     O   H O L A N D Ê S       ")
        print("--------------------------------")
        print(" PEDIDO Nº: ",contador)
        print("===========================")
        nome = input("Digite seu nome: ")
        print("Escolha seu prato:")
        print("[1] Tradicional - Arroz, Feijão, Farofa, Batata Frita, ")
        print("                  Bife de Frango ou Lombo e Salada.")
        print("                  Bife de boi tem acréscimo de R$ 4,00.")
        print("")
        print("[2] Fitness     - Arroz Integral, Purê de Batata Doce,")
        print("                  Salada, Filé de Peixe ou Frango.")
        print("")
        print("[3] do Dia      - (seg) Lasanha, (ter) Frango a Milanesa,")
        print("                  (qua) Tropeiro, (qui) Strogonoff,")
        print("                  (sex) Feijoada, (sab) Batata Recheada.")
        pedido = input("Digite seu Pedido: ")
        pedido = str(pedido)
        if pedido == "1":
            pedido1 = input(" Você deseja o TRADICIONAL com qual carne? [1]Frango, [2]Lombo ou [3]Alcatra")
            pedido1 = str(pedido1)
            if pedido1 == "1":
                prato = ("Tradicional com Frango")
                valorprato = 15.90
            elif pedido1 == "2":
                prato = ("Tradicional com Lombo")
                valorprato = 15.90
            else:
                prato = ("Tradicional com Alcatra")
                valorprato = 19.90
            resposta = input("Você deseja fazer alguma troca ou alteração no prato?[S/N]")
            if resposta == "S" or resposta == "s":
                alteracao = input("Qual alteração ou troca você deseja fazer? ")
        if pedido == "2":
            pedido1 = input(" Você deseja o FITNESS com qual carne? [1]Frango [2]Peixe")
            pedido1 = str(pedido1)
            if pedido1 == "1":
                prato = ("Fitness com Frango")
                valorprato = 15.90
            elif pedido1 == "2":
                prato = ("Fitness com Peixe")
                valorprato = 15.90
            resposta = input("Você deseja fazer alguma troca ou alteração no prato?[S/N]")
            if resposta == "S" or resposta == "s":
                alteracao = input("Qual alteração ou troca você deseja fazer? ")
        if pedido == "3":
            print("Você escolheu o Prato do Dia")
            prato = ("Prato do Dia")
            valorprato = 15.90
            resposta = input("Você deseja fazer alguma troca ou alteração no prato?[S/N]")
            if resposta == "S" or resposta == "s":
                alteracao = input("Qual alteração ou troca você deseja fazer? ")
        if (alteracao == "") or (alteracao == "N"):
            alteracao = ("nenhuma alteração")

        resposta1 = input("Você deseja beber algo ? [S/N] ")
        if resposta1 == "S" or resposta1 == "s":
            print("Qual bebida você deseja tomar ? ")
            resposta2 = input(" [1] Agua  [2] Refrigerante 350ml [3] Suco Natural ")
            if resposta2 == "1":
                bebida = str(bebida)
                bebida = "Água Mineral"
                valorprato = valorprato + 5
            elif resposta2 == "2":
                bebida = "Refrigerante"
                valorprato = valorprato + 5
            elif resposta2 == "3":
                bebida = "Suco Natural"
                valorprato = valorprato + 5
        if (bebida == "") or (bebida == "N"):
            bebida = ("nenhuma bebida")
        clear()
        print("")
        print("===============================================")
        print("             CONFIRMAÇÃO DE PEDIDO             ")
        print("===============================================")
        print(" Confirmando seu pedido ", nome)
        print(" Foi um ", prato, " com ", bebida)
        print(" com a observação de ", alteracao)
        print("O total foi de R$ ", valorprato)
        confirmacao = input("Posso confirmar seu pedido ? [S/N]")
        if confirmacao == "S" or confirmacao == "s":
            contador += 1
            clear()
            break
        else:
            clear()
            continue
    if nome == "fechadototem":
        break



print("===============================================")
print("                FECHAMENTO DO DIA              ")
print("===============================================")
print("Foram pedidos ", contador, " pratos")
input("Deseja fechar ?")
