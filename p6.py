print("Insira seu peso")
peso = float(input())

print("Insira sua altura")
altura = float(input())

imc = peso/(altura*altura)

if imc>30:
    print("O usuario esta obeso")

else:
    print("O usuario esta abaixo da linha da obesidade")