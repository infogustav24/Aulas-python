idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida.")
elif idade < 12 or idade >= 60:
    print("Entrada gratuita.")
else:
    print("Valor da entrada: R$ 20,00")
