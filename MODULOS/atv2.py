#faça uma programa que peça o cateto oposto, adjacente, e calcule a hipotenusa
import math

n1 = float(input("digite o valor do primeiro cateto: "))
n2 = float(input("digite o valor do segundo cateto: "))
catetos = math.pow(n1,2) + math.pow(n2,2) 

print(" o valor da soma dos catetos é {:.2f} e a hipotenusua é {:.2f}".format(catetos,math.sqrt(catetos)))