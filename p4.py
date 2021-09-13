print("Insira dois numeros")
perfeito1 = int(input())
perfeito2 = int(input())

flag1=0
flag2=0

for i in range(1,perfeito1-1):
  if perfeito1%i==0:
			flag1+=i

for z in range(1,perfeito2):
  if perfeito2%z==0:
			flag2+=z

if perfeito1==flag1 and perfeito2==flag2:
  print("Sao divisores perfeitos")

else:
  print("Nao sao divisores perfeitos")
