print("Insira o custo de producao")
custo = float(input())

distribuidor = custo*0.28
imposto = custo*0.45

consumidorpaga = custo + distribuidor + imposto

print(consumidorpaga)