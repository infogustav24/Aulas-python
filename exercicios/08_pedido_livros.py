estoque = 8
quantidade = int(input("Quantos exemplares deseja retirar? "))

if quantidade <= 0:
    print("Pedido inválido.")
elif quantidade > estoque:
    print("Não há exemplares suficientes.")
else:
    estoque -= quantidade
    print("Pedido confirmado.")
    print(f"Quantidade restante: {estoque}")
