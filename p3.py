print("Insira as notas das provas e do trabalho")
prova1 = int(input())
prova2 = int(input())
trabalho = int(input())

prova1 = prova1*3
prova2 = prova2*3

if (prova1+prova2+trabalho)/7 >= 7:
    print("Aprovado")
else:
    print("Reprovado")