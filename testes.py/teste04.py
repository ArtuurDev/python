
import math



cateto_adjacente = float(input("informe o valor do cateto adjacente:"))
cateto_oposto = float(input("informe o valor do cateto oposto:"))

print("o valor informado do cateto_adjacente é:", cateto_adjacente)
print("o valor do cateto oposto é:",cateto_oposto)

calculo_catetos = (cateto_adjacente **2) + (cateto_oposto **2)
print(calculo_catetos)


raiz =  math.sqrt(calculo_catetos)

print(" o valor da hipotenusa é:", raiz)