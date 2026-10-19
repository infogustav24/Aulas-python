idade = int(input("Digite sua idade: "))
inscricao = input("Você possui inscrição? (sim/nao): ")

if idade >= 14 and inscricao == "sim":
    print("Entrada permitida.")
else:
    print("Entrada não permitida.")