#faça um progrma q leia o salario de um usuario e o valor de reajuste da porcentagem

s = float(input("digite seu salario: "))
p = float(input("quantos porcento? "))
print("seu salario é {} com reajuste é {:.2f}".format(s, s * p / 100 + s))