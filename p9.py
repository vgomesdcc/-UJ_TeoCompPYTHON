print("Insira o tempo em segundos")
s = int(input())

horas = s/3600
resto = s%3600

minutos = resto/60
segundos = resto%60

print("Hora(s):")
print(int(horas))
print("Minuto(s):")
print(int(minutos))
print("Segundo(s):")
print(int(segundos))