""" nome= input("Digite o teu nome")
print(f"Olá {nome} Seja bem-vindo(a)!")
nome = input("Nome: ")
cidade = input("Cidade: ")
idade= input("Digite a tua idade")
print("=== CADASTRO ===")
print("Nome:", nome)
print("Cidade:", cidade)
print("idade",idade)
print(type(idade))

primeira forma de converção 

idade_texto = input("Digite sua idade: ")
idade = int(idade_texto)
print("----------------------------")
print("----------------------------")
print(f"Tipo da variavel = idade texto: {type(idade_texto)} ")
print(f"Tipo da variavel = idade texto: {type(idade)} ")
print("----------------------------")
print("----------------------------")
print("No proximo aniver tu tera",idade + 1,"anos")
print("----------------------------")
print("----------------------------")
 
# Segunda forma de converção
Idade = int(input("Digite sua idade: "))
print(f"Tipo da variavel = idade {type(Idade)} ")
print("No proximo aniver tu tera",Idade + 1,"anos")
print("-----------------------------")
print("-----------------------------")

preco = float(input("Preço do produto: "))
quantidade = int(input("Quantidade: "))
total = preco * quantidade
print("Total da compra:", total)

idade = 18          # Atribui um valor.
print(idade == 18)   # Compara o valor e mostra True.
resposta = input("Deseja continuar? Digite sim ou nao: ")
print(resposta == "sim")

idade = int(input("Digite sua idade: "))

 if idade >= 18:
    print("Você atingiu a maioridade.")

print("Consulta encerrada.")

energia = int(input("Energia do robô: "))

if energia < 20:
    print("Energia baixa.")
    print("Procure uma estação de recarga.")

print("Verificação concluída.") """


media = float(input("Digite a média de 0 a 10: "))

if media >= 7:
    print(f"Media:{media:.2f}Aprovado.")
elif media >= 5:
    print(f"Media:{media:.2f}Em recuperação.")
else:
    print(f"Media:{media:.2f}Reprovado.")

print("------------------------------")
print("------------------------------")

temperatura = float(input("Temperatura: "))

if temperatura >= 36:
    print("Calor intenso.")

elif temperatura >= 30:
    print("Dia quente..")

print("-----------------------")
print("------------------------")

""" idade = int(input("Idade: "))
vagas = int(input("Vagas disponíveis: "))

if idade >= 14 and vagas > 0:
    print("Inscrição permitida.")
else:
    print("Inscrição não permitida.")

print("-----------------------")
print("------------------------") 

temIgresso= True
idade = int(input("Digita a tua idade"))
if idade >= 18 or temIgresso==True:
 print ("Pode entrar na feta!")
else:
  print("Não pode entrar na feta!") """

idade = 16
categoria = "estudante"

if idade >= 14 and (categoria == "estudante" or categoria == "professor"):
    print("Pode participar da atividade.")