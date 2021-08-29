print("Insira seu salario")
salario = float(input())

if salario<=1903.98:
    string = repr(salario)
    print("seu salario liquido e R$ "+string+" Voce esta insento do imposto")

elif salario>1903.99 and salario<=2826.65:
    salario = salario-(salario*0.075)
    string = repr(salario)
    print("seu salario liquido e R$ "+string+" voce foi tributado em 7,5%")

elif salario>=2826.66 and salario<=3751.05:
    salario = salario-(salario*0.15)
    string = repr(salario)
    print("seu salario liquido e R$ "+string+" voce foi tributado em 15%")

elif salario>=3751.06 and salario<=4664.68:
    salario = salario-(salario*0.225)
    string = repr(salario)
    print("seu salario liquido e R$ "+string+" voce foi tributado em 22,5%")

elif salario>=4664.69:
    salario = salario-(salario*0.275)
    string = repr(salario)
    print("seu salario liquido e R$ "+string+" voce foi tributado em 27,5%")