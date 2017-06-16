#__main__
contador = 1
nome = ""
alteracao = ""
bebida = ""
pedido = ""
prato = ""
valorprato = float
resposta = ""
resposta2 = ""
custocomida = float
valortotal = float

def mostrador(cont):
    print("--------------------------------")
    print(" SEJA BEM VINDO AO RESTAURANTE ")
    print("     O   H O L A N D Ê S       ")
    print("--------------------------------")
    print(" PEDIDO Nº: ",cont)
    print("===========================")
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







def pratos(prato):
    if pedido == "1":
        pedido1 = input(" Você deseja o TRADICIONAL com qual carne? [1]Frango, [2]Lombo ou [3]Alcatra  ")
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
    if pedido == "2":
        pedido1 = input(" Você deseja o FITNESS com qual carne? [1]Frango [2]Peixe  ")
        pedido1 = str(pedido1)
        if pedido1 == "1":
            prato = ("Fitness com Frango")
            valorprato = 15.90
        elif pedido1 == "2":
            prato = ("Fitness com Peixe")
            valorprato = 15.90
    if pedido == "3":
        print("Você escolheu o Prato do Dia")
        prato = ("Prato do Dia")
        valorprato = 15.90
    return prato

def nomebebida(x):
    if x == "S" or x == "s":
        print("Qual bebida você deseja tomar ? ")
        resposta2 = input(" [1] Agua  [2] Refrigerante 350ml [3] Suco Natural ")
        if resposta2 == "1":
            bebida = "Água Mineral"
        elif resposta2 == "2":
            bebida = "Refrigerante"
        elif resposta2 == "3":
            bebida = "Suco Natural"
    else:
        bebida = ("nenhuma bebida")

    y = bebida
    return y


def precocomida(x):
    if x == "Tradicional com Frango":
        custocomida = 15.9
    elif x == "Tradicional com Lombo":
        custocomida = 15.9
    elif x == "Tradicional com Alcatra":
        custocomida = 19.9
    elif x == "Fitness com Frango":
        custocomida = 15.9
    elif x == "Fitness com Peixe":
        custocomida = 15.9
    elif x == "Prato do Dia":
        custocomida = 15.9
    y = custocomida
    return y


def precobebida(x):
    if x == "Água Mineral":
        custobebida = 5.0
    elif x == "Refrigerante":
        custobebida = 5.0
    elif x == "Suco Natural":
        custobebida = 5.0
    else:
        custobebida = 0

    y = custobebida
    return y
    

def alteracao(x):
    if x == "S" or x == "s":
        resposta = input('Qual alteração deseja fazer ? ')
    elif x == "" or x == "N" or x =="n":
        resposta = ("nenhuma alteração")
    y = resposta
    return y



def confirmacao():
    print("")
    print("===============================================")
    print("             CONFIRMAÇÃO DE PEDIDO             ")
    print("===============================================")
    print("")
    print("Confirmando seu pedido", nome)
    print("")
    print("Foi um {} com {}".format(x,beb))
    print("com a observação de ", alt)
    print("O total foi de R$ ", valortotal)










cont = 1
while True:
    while True:
        mostrador(cont)
        nome = input("Digite seu nome: ")
        pedido = input("Digite seu Pedido: ")
        x = pratos(prato)
        precoc = precocomida(x)
        resposta = input("Você deseja fazer alguma troca ou alteração no prato?[S/N]")
        alt = alteracao(resposta)
        resposta1 = input("Você deseja beber algo ? [S/N] ")
        beb = nomebebida(resposta1)
        precob = precobebida(beb)
        valortotal = precoc + precob
        confirmacao()
        confirmacao1 = input("Posso confirmar seu pedido ? [S/N]")
        if confirmacao1 == "S" or confirmacao1 == "s":
            cont += 1
            break
        else:
            continue
    if nome == "fechadototem":
        break










print("===============================================")
print("                FECHAMENTO DO DIA              ")
print("===============================================")
print("Foram pedidos ", contador, " pratos")
input("Deseja fechar ?")
