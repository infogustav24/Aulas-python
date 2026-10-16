""" idade = 10
categoria = "Professor"

if idade >= 14 and (categoria == "estudante" or categoria == "professor"):
    print("Pode participar da atividade.")
else:
    print("Não dá participar da atividade.") 
resposta = input("O robô está em manutenção? (sim/nao): ")
em_manutencao = resposta == "sim"

if not em_manutencao:
    print("Robô disponível para uma missão.")
else:
    print("Aguarde o fim da manutenção.")

print("-------------------------------------")
print("-------------------------------------")
quantidade = int(input("Quantidade desejada: "))
estoque = 10

if quantidade > 0:
    if quantidade <= estoque:
        estoque = estoque - quantidade
        print("Pedido confirmado.")
        print("Estoque restante:", estoque)
    else:
        print("Estoque insuficiente.")
else:
    print("A quantidade deve ser maior que zero.")
    """

print("-------------------------------------")
print("-------------------------------------")
nome = input("Nome do robô: ")
energia = int(input("Energia atual (0 a 100): "))
resposta = input("Está em manutenção? (sim/nao): ")

print("=== CENTRAL DE MISSÕES ===")
print("Robô:", nome)

if energia < 0 or energia > 100:
    print("Energia inválida. Informe um valor entre 0 e 100.")
elif resposta != "sim" and resposta != "nao":
    print("Resposta inválida. Use sim ou nao.")
else:
    em_manutencao = resposta == "sim"

    if energia >= 50 and not em_manutencao:
        print("Missão autorizada.")
        energia = energia - 30
        print("Energia após a missão:", energia)
    elif em_manutencao:
        print("Missão bloqueada: robô em manutenção.")
    else:
        print("Missão bloqueada: energia insuficiente.")

print("Atendimento encerrado.")