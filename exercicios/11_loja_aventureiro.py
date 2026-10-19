nome = input("Nome do aventureiro: ")
ouro = int(input("Quantidade de ouro: "))

if ouro < 0:
    print("Quantidade de ouro inválida")
else:
    print("1 - Poção de vida (25 moedas)")
    print("2 - Escudo (60 moedas)")
    print("3 - Espada (100 moedas)")
    opcao = input("Escolha um item: ")

    itens = {
        "1": ("poção de vida", 25),
        "2": ("escudo", 60),
        "3": ("espada", 100),
    }

    if opcao not in itens:
        print("Item inválido")
    else:
        item, preco = itens[opcao]
        if ouro >= preco:
            ouro -= preco
            print(f"{nome} adquiriu {item}.")
            print(f"Saldo restante: {ouro} moedas.")
        else:
            print(f"Saldo insuficiente. Faltam {preco - ouro} moedas.")