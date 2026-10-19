numero1 = float(input("Digite o primeiro número decimal: "))
numero2 = float(input("Digite o segundo número decimal: "))

print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
opcao = input("Escolha uma opção: ")

if opcao == "1":
    print(f"Resultado: {numero1 + numero2}")
elif opcao == "2":
    print(f"Resultado: {numero1 - numero2}")
elif opcao == "3":
    print(f"Resultado: {numero1 * numero2}")
elif opcao == "4":
    if numero2 == 0:
        print("Não é possível dividir por zero")
    else:
        print(f"Resultado: {numero1 / numero2}")
else:
    print("Opção inválida")
