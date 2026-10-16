# Exercício 13 - Cadastro de uma oficina

nome = "Robótica para iniciantes"
sala = "Laboratório de Robótica"
contato = 24
horas = 24
inscricao = True

print("Nome da oficina:", nome)
print("Sala:", sala)
print("Contato:", contato)
print("Horas:", horas)
print("Inscrição aberta:", inscricao)

print(type(nome))
print(type(sala))
print(type(contato))
print(type(horas))
print(type(inscricao))

# Exercício 14 - Dividindo a conta

pizza = 48
bebida = 12
amigos = 4

total = pizza + bebida
por_amigo = total / amigos

print("Preço da pizza:", pizza)
print("Preço da bebida:", bebida)
print("Número de amigos:", amigos)
print("Total da conta:", total)
print("Valor por amigo:", por_amigo)

print(type(amigos))
print(type(por_amigo))

# Exercício 15 - Estoque da biblioteca

livros = 40
novos = 12
devolvidos = 4
emprestados = 6

total = livros + novos + devolvidos - emprestados

print("Livros disponíveis:", livros)
print("Livros novos:", novos)
print("Livros devolvidos:", devolvidos)
print("Livros emprestados:", emprestados)
print("Total de livros:", total)

# Exercício 16 - Boletim de notas

aluno = 10

nota1 = 7.5
nota2 = 8.0
nota3 = 9.5

soma = nota1 + nota2 + nota3
media = soma / 3

print("Aluno:", aluno)
print("Soma das notas:", soma)
print("Média:", media)

print(type(soma))
print(type(media))

# Exercício 16 - Boletim de notas

aluno = 10

nota1 = 7.5
nota2 = 8.0
nota3 = 9.5

soma = nota1 + nota2 + nota3
media = soma / 3

print("Aluno:", aluno)
print("Soma das notas:", soma)
print("Média:", media)

print(type(soma))
print(type(media))

# Exercício 18 - Guardando o valor anterior

saldo = 80
saldo_anterior = saldo

saldo = saldo - 25
saldo = saldo + 10

print("Saldo anterior:", saldo_anterior)
print("Saldo atual:", saldo)

print(type(saldo_anterior))
print(type(saldo))

# Exercício 19 - Orçamento do passeio

alunos = 20
onibus = 600
entrada = 15
lanche = 10

ingressos = alunos * entrada
lanches = alunos * lanche

total = onibus + ingressos + lanches
por_aluno = total / alunos

print("Número de alunos:", alunos)
print("Custo do ônibus:", onibus)
print("Total dos ingressos:", ingressos)
print("Total dos lanches:", lanches)
print("Custo total:", total)
print("Valor por aluno:", por_aluno)

print(type(total))
print(type(por_aluno))

# Exercício 20 - Tipos de dados

texto = "42"
inteiro = 42
decimal = 42.0
booleano = False

print("Texto:", texto)
print("Inteiro:", inteiro)
print("Decimal:", decimal)
print("Booleano:", booleano)

print(type(texto))
print(type(inteiro))
print(type(decimal))
print(type(booleano))

# Exercício 21 - Robô explorador

nome = "C3D2"
distancia = 0
energia = 100
amostras = 0
missao = True
tempo = 4

print("-----Amigo Robo")
print("nome:",nome)
print("Distância inicial:", distancia)
print("Energia inicial:", energia)

distancia = distancia + 120
energia = energia - 20

print("O robô andou 120 metros")
print("Distância:", distancia)
print("Energia:", energia)

amostras = amostras + 3
energia = energia - 15

print("Amostras coletadas:", amostras)
print("Energia:", energia)

energia = energia + 10

print("Energia recarregada:", energia)

distancia = distancia + 80
energia = energia - 25

print("Distância:", distancia)
print("Energia:", energia)

amostras = amostras + 2
energia = energia - 10

print("Amostras coletadas:", amostras)
print("Energia:", energia)

missao = False

media = distancia / tempo

print("Distância final:", distancia)
print("Energia final:", energia)
print("Total de amostras:", amostras)
print("Missão ativa:", missao)
print("Média por minuto:", media)