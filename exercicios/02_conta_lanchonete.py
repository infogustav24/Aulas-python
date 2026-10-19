preco = float(input("Digite o preço do lanche: R$ "))
quantidade = int(input("Digite a quantidade comprada: "))

if preco <= 0 or quantidade <= 0:
    print("Erro: o preço e a quantidade devem ser positivos.")

else:
    total = preco * quantidade

    if total >= 50:
        desconto = total * 0.10
    else:
        desconto = 0

    valor_final = total - desconto

    print("\===== CONTA DA LANCHONETE =====")
    print(f"Total antes do desconto: R$ {total:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
    print("===============================")