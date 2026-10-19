nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 <0 or nota1 > 100:
    print("nota invalida. Informa uma nota entre 0 e 10.")
    
elif nota1 >= 7:
     print("Aprovado")
elif nota1 >= 5:
     print("Recuperação")
else:
   
     print("Reprovado")
 
   